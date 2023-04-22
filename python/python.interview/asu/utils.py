import glob
import os
import cv2
import time
import itertools
import numpy as np
import tensorflow as tf
import scipy
import keras.backend as K
from keras import Model
from keras.applications import VGG19

def load_images_from_directory(images_directory: str, images_extension: str, images_dimension: tuple) -> tuple[object, list]:
    """
    @author: Vo Huynh Quang Nguyen
    Load all images having the same extension and dimension in a directory.

    This function load_images_from_directory load all images having the same extension and dimension in a directory by leveraging the Unix style pathname pattern expansion.
    
    @param images_directory: Unix style pathname. The default value is './dataset/images'
    @param images_extension: Unix style user-specific image extension ('*.png', '*.jpg', '*.bmp', etc.).
    @param images_dimension: Image dimension (width, height).

    @return images: Array containing loaded images.
    @return image_paths: List containing relative path to individual images.
    """
    path = os.path.join(images_directory, images_extension)
    image_fnames = glob.glob(path)
    
    images = []
    image_paths = []
    for _ , image_fname in enumerate(image_fnames):
        image = cv2.imread(image_fname, cv2.IMREAD_UNCHANGED)
        if (image.shape == images_dimension):
            images.append(image)
            image_paths.append(image_fname)
        
    return np.array(images), image_paths

def export_images_to_other_extensions(images: object, image_paths: list, new_extension: str) -> None:
    """
    @author: Vo, Huynh Quang Nguyen

    Export images to other extensions.

    This function export_images_to_other_extensions export input images to other user-specified extensions.

    @param images: Array containing images.
    @param image_paths: List containing relative path to individual images.
    @param new_extension: User-specified extension.
    """
    
    for image_path, image in zip(image_paths, images):
        relative_path, _ = os.path.splitext(image_path)
        new_image_fname = os.path.join(relative_path + new_extension)
        cv2.imwrite(new_image_fname, image)

    return None

def resize_images(input_images: object, desired_shape: tuple) -> object:
    """
    @author: Vo, Huynh Quang Nguyen

    Resize image to a desired dimension.

    This function resize_images resizes individual image from an array containing images to a desired dimension.
    @param input_images: Array containing input images.
    @param desired_shape: Desired dimension (height, width).
    @return output_images: Array containing resized images.
    """
    
    output_images = []
    for image in input_images:
        if (image.shape == desired_shape):
            output_image = image
            output_images.append(output_image)
        else:
            output_image = cv2.resize(image, desired_shape, cv2.INTER_CUBIC)
            output_images.append(output_image)
    
    return output_images

def normalize_and_convert_uint8(images: object) -> object:
    """
    @author: Vo, Huynh Quang Nguyen

    Normalize and convert image to unsigned 8-bit integer data type.

    This function normalize_and_convert_uint8 normalizes and convert each individual image in an array of images to [0-255] range and unsigned 8-bit integer data type, respectively.
    
    @param images: Array containing input images.
    @return finals: Array containing normalized images.
    """
    
    mask = np.zeros(images[0].shape)
    finals = []
    
    for image in images:
        normalized = cv2.normalize(image, mask, 0, 255, cv2.NORM_MINMAX)
        normalized = normalized.astype('uint8')
        finals.append(normalized)

    return np.array(finals)

def compute_histogram(image: object) -> object:
    """
    @author: Vo, Huynh Quang Nguyen

    Compute histogram of an image.

    This function compute_histogram compute the histogram of a 8-bit grayscale image.
    
    @param image: Input image.
    @return histogram: Computed histogram of the input image.
    """
    
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    
    return histogram
    
def image_segmentation(image: object, clahe_size: int = 21, ksize: int = 5, 
    threshold_bright: int = 180, threshold_dark: int = 40, morph_ksize: int = 3) -> tuple[object, object, object, object, object]:
    """
    @author: Vo, Huynh Quang Nguyen

    Segment images into instances.

    This function image_segmentation employs basic image processing techniques to segment images into multiple regions. The employed techniques are:
    1. Background removal;
    2. Histogram equalization;
    3. Thresholding;
    4. Morphological operation;
    5. Contour detection and filling.

    @param image: Input image
    @param clahe_size: Tilt size for contrast limited adaptive histogram equalization (CLAHE) method.
    @param ksize: Kernel size for lowpass filtering.
    @param threshold_bright: Thresholding value for images having smaller cumulative defect size areas.
    @param threshold_dark: Thresholding value for images having larger cumulative defect size areas.
    @param morph_ksize: Kernel size for morphological operation.
    @return result: Final result of the segmentation.
    @return equalized: Result of the CLAHE method.
    @return blur: Result of the lowpass filtering method.
    @return thresh: Result of the thresholding method
    @return morph: Result of the morphological operations.
    """
    ##
    # Background removal:
    #
    result = image.copy()
    mask = np.zeros(image[0].shape)
    image[image == 0] = 255
    
    ##
    # Histogram Equalization:
    #
    tileGridSize = (clahe_size, clahe_size)
    clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize = tileGridSize)
    equalized = clahe.apply(image) 

    ##
    # Remove highpass components:
    #
    blur = cv2.medianBlur(image, ksize = ksize)
    
    ##
    # Pixel median:
    #
    median = np.median(image.ravel())
    if (median > 200):
        ##
        # Thresholding:
        #
        blur = cv2.medianBlur(image, ksize = ksize)
        _ , thresh = cv2.threshold(blur, threshold_bright, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    else:
        ##
        # Thresholding:
        #
        blur = cv2.medianBlur(image, ksize = ksize)
        _ , thresh = cv2.threshold(blur, threshold_dark, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    ##
    # Morphological operation:
    #
    kernel = np.ones((morph_ksize, morph_ksize))
    morph = cv2.morphologyEx(thresh, cv2.MORPH_DILATE, kernel = kernel, iterations = 1)

    ##
    # Contour detection:
    #
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    result = cv2.fillPoly(result, pts = contours, color = (0, 0, 0))

    return result, equalized, blur, thresh, morph


def estimate_execution_time(images: object):
    """
    @author: Vo, Huynh Quang Nguyen

    Estimate execution time of a method.

    This function estimate_execution_time estimates the execution time of an image processing method by:
    1. Iterating this method for all possible permutations of a subset.
    2. Measuring the execution time for each iteration.
    3. Compute the mean execution time.

    @param images: Array containing input images.
    @return estimated_execution_time: Estimated execution time in seconds.
    """
    
    permutations = itertools.permutations(list(range(images.shape[0])))
    times = []
    for set in permutations:
        for idx in set:
            start = time.time()
            image_segmentation(images[idx])
            end = time.time()
            estimated_time = abs(start - end)
            times.append(estimated_time)
    estimated_execution_time = np.mean(np.array(times), axis = -1)
    
    return estimated_execution_time

def estimated_mse(input_image: object, output_image: object) -> float:
    """
    @author: Vo, Huynh Quang Nguyen

    Estimate the mean squared error (MSE) between two images.

    This function estimated_mse estimates the MSE between two flattening images, respectively.

    @param input_image: Input image.
    @param output_image: Output image.
    @return mse: Computed MSE.
    """  
    
    mse = round(np.mean((input_image.ravel()- output_image.ravel()) ** 2, axis = -1), 4)
    
    return mse

def feature_extractor() -> object:
    """
    @author: Vo, Huynh Quang Nguyen

    Implement a feature extractor for computing perceptual loss.
    
    This function feature_extractor implements a TensorFlow feature extractor model for computing perceptual loss. The model architecture is pretrained no-top VGG19 network.

    @return model: Keras API model.
    """
    
    selected_layers = ['block1_conv1', 'block2_conv2',"block3_conv3" ,'block4_conv3','block5_conv4']

    vgg19 = VGG19(weights = 'imagenet', include_top = False, input_shape = (1010, 1010, 3))
    vgg19.trainable = 'False'
    outputs = [vgg19.get_layer(l).output for l in selected_layers]
    model = Model(vgg19.input, outputs)
    
    return model

vgg19 = feature_extractor()

def preproccess_image(image: object) -> object:
    """
    @author: Vo, Huynh Quang Nguyen

    Preprocess image before applying feature extraction.

    This function preproccess_image preprocesses an input image before applying feature extraction by:
    1. Transforming the input image from 1-channel to 3-channel;
    2. Resize the input image's dimension to (1010,1010);
    3. Normalize image to range [0.0, 1.0].

    @param image: Input image.
    @return image: Preprocessed image.
    """
    
    image = np.stack((image,) * 3, axis = -1)
    image = tf.image.resize(image, size = (1010, 1010), method = 'bicubic')
    image = image.numpy() / 255.0
    
    return image

@tf.function
def fmap_subtraction(input_image: object, output_image: object) -> object:
    """
    @author: Vo, Huynh Quang Nguyen

    Compute the difference between input image's and output image' feature maps, respectively.

    This function fmap_subtraction generates a heatmap that is the weighted squared difference between input image's and output image' feature maps, respectively.

    @param input_image: Input image.
    @param output_images: Output image.
    @return hmaps: List containing generated heatmaps.
    """

    selected_layer_weights = [1.0, 2.0 , 4.0 , 8.0 , 16.0]
    selected_layer_filters = [64, 128, 256, 512, 512]
    
    input_features = vgg19(input_image[None])
    output_features = vgg19(output_image[None])

    hmaps = []
    for input_feature, output_feature, weight, n_filters in zip(input_features, output_features, selected_layer_weights, selected_layer_filters):
        hmap = weight * K.sum(K.square(input_feature - output_feature), axis = -1) /  n_filters
        hmaps.append(hmap)

    return hmaps

def fmap_reconstruction(hmaps: object) -> object:
    """
    @author: Vo, Huynh Quang Nguyen

    Reconstruct and transform all heatmaps to create a united heatmap.

    This function fmap_reconstruction reconstructs and transforms all generated heatmaps to create a united heatmap.

    @param hmaps: List containing generated heatmaps.
    @return result: United heatmap.
    """
    
    new_hmaps = []
    for hmap in hmaps:
        new_hmap = scipy.ndimage.zoom(hmap, (1, 1010 / hmap.shape[1], 1010 / hmap.shape[2]), order = 2)
        new_hmaps.append(new_hmap)
    result = np.mean(new_hmaps, axis = 0)
    
    return result[0]

