# A guide to quickly install Anaconda and TensorFlow

💡 This guide is inspired by the [video lecture](https://www.youtube.com/watch?v=OEFKlRSd8Ic) given by Dr. Jeff Heaton from Washington University of St. Louis.

***

# 1. Python Setup
First, we must understand what an IDE means. So, what is an IDE? 
1. An **integrated development environment** (IDE) is software for building applications that combine common developer tools into a single graphical user interface (GUI). 
2. An IDE typically consists of:
    - **Source code edito**r: A text editor that can assist in writing software code with features such as syntax highlighting with visual cues, providing language-specific auto-completion, and checking for bugs as code is being written.
    - **Local build automation**: Utilities that automate simple, repeatable tasks as part of creating a local build of the software for use by the developer, like compiling computer source code into binary code, packaging binary code, and running automated tests.
    - **Debugger**: A program for testing other programs that can graphically display the location of a bug in the original code.
3. One of the most common IDEs is Microsoft Visual Studio Code. It can be downloaded and installed [here](https://code.visualstudio.com/).

When searching for information on Python, you usually hear the following phrases: **Python implementation**, **Python distribution**, **Python dependencies**, and **Python** itself. So exactly what are these?
1. **Python itself**: When referring to Python itself, we only consider the set of rules that are defined in [Python.org](http://python.org/), i.e. the behaviors associated with Python.
2. **Python implementation**: When referring to Python implementation, we are considering the actual program (e.g., [CPython](https://en.wikipedia.org/wiki/CPython#:~:text=CPython%20is%20the%20reference%20implementation,Guido%20van%20Rossum)) that provides such behaviors.
3. **Python distribution**: When referring to Python distribution, we are considering (1) Python implementations and (2) accompanying tools and libraries.
4. **Python dependencies**: When referring to Python dependencies, we are considering all necessary software components that are needed for our work.

|  | Description | Analogy |
| --- | --- | --- |
| **Python itself** | Python behaviors/syntax/etc. | Grammatical rules of a language (e.g., English), or a description of what a machine (e.g., an oven) does |
| **Python implementation** | The actual program that runs the language | People that use such language (e.g., English), or an actual machine (e.g., an oven) |
| **Python distribution** | Python implementations, and accompanied tools and libraries | A fully equipped kitchen (e.g., oven + cooking utensils) |
| **Python dependencies** | Necessary Python-based software components | Ingredients + a machine + tools to complete a task (e.g., cook food) |

In this guide, we are only concerned with Python distribution. There are two primary Python distributions: **Anaconda** (a.k.a conda), and **Package Installer for Python** (a.k.a pip). Their differences are as follows:

| conda | pip |
| --- | --- |
| Install packages (i.e. libraries) and software that are Python and other languages → no need to install the compiler (since it already comes with the distribution). | Install only packages (i.e. libraries) that are Python → A compiler needs to be installed first. |
| Can create containers, i.e., isolated environments that can contain different versions of Python and/or installed packages. |  |
| When installing packages, a solver is run to ensure all requirements of all packages installed in an environment are met. | When installing packages, no effort is made to ensure that the dependencies of all packages are fulfilled simultaneously. |

In this guide, we will use the Anaconda distribution to set up our Python and link Anaconda with Visual Studio Code. The steps are as follows:
1. [Install Anaconda as normal.](https://www.anaconda.com/)
2. Open `Edit the system environment variables`>`Environment variables`. On the `System variables` section, click `Path` and then add the following paths
        
        `C:\ProgramData\Anaconda3\Scripts`
        
        `C:\ProgramData\Anaconda3\Library\bin`
        
2. Open `Windows Powershell`(remember to run this program with the **Run as Administrators** option), and use the command `Set-ExecutionPolicy RemoteSigned` to change the Powershell Execution Policy to Remote Signed.
    
    ![Figure 4: Change the `ExecutionPolicy` to `RemoteSigned`.](A%20guide%20to%20quickly%20install%20Anaconda%20and%20TensorFlow%20419684ec9f034aa781cc3a2be5061acd/Untitled%201.png)
    
    Figure 4: Change the `ExecutionPolicy` to `RemoteSigned`.
    
3. Open Anaconda Prompt (Run as Administrators) and run the command `conda init powershell` to add conda-related startup to a Powershell profile.
    
    ![Figure 5: Add conda-related startup to Windows Powershell.](A%20guide%20to%20quickly%20install%20Anaconda%20and%20TensorFlow%20419684ec9f034aa781cc3a2be5061acd/Untitled%202.png)
    
    Figure 5: Add conda-related startup to Windows Powershell.
    

![Figure 2: When installing Python using Anaconda, we need to opt for the option `All Users` to ensure every user that uses the computer will have the same distribution version.](A%20guide%20to%20quickly%20install%20Anaconda%20and%20TensorFlow%20419684ec9f034aa781cc3a2be5061acd/Untitled%203.png)

Figure 2: When installing Python using Anaconda, we need to opt for the option `All Users` to ensure every user that uses the computer will have the same distribution version.

![Figure 3: Add these paths to the `System Environment Variables`.](A%20guide%20to%20quickly%20install%20Anaconda%20and%20TensorFlow%20419684ec9f034aa781cc3a2be5061acd/Untitled%204.png)

Figure 3: Add these paths to the `System Environment Variables`.

1. To remove unused kernels in Anaconda.
    1. Go to Anaconda Prompt.
    2. Run `jupyter kernelspec list` to get the paths of all installed kernels.
    3. Uninstall unwanted kernel with the following command: `jupyter kernelspec uninstall <unwanted-kernel>`
