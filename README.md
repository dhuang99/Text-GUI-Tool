<!-- Project Title -->
<h2 align="left">Text GUI Tool</h2>
<p align="left">A Python GUI that copies email templates into the user's clipboard.</p>


<!-- Table of Contents -->
<h2 style="display: inline-block">Table of Contents</h2>
<ol> 
	<li>
		<a href="#about-the-project">About The Project</a>
	</li>
	<li><a href="#getting-started">Gettings Started</a>
		<ul>
			<li> <a href="#prerequisites">Prerequisites</a> </li>
			<li> <a href="#installation">Installation</a> </li>
		</ul>
	</li>
	<li><a href="#usage">Usage</a></li>
		<ul>
			<li> <a href="#executing-the-script">Executing the Script</a> </li>
			<li> <a href="#using-the-gui">Using the GUI</a> </li>
		</ul>
	<li><a href="#road-map">Road Map</a>
		<ul>
			<li> <a href="#potential-features">Potential Features</a> </li>
			<li> <a href="#known-issues">Known Issues</a> </li>
		</ul>
	</li>
			
</ol>		
	

## About The Project
At my part-time during University, I was suddenly given the responsiblity of helping manage the store side of the IT department. We had an online store which managed transactions with faculty and staff through a centralized Gmail. 
</br> </br>
As a store manager, I had to go through the e-commerce process with each customer. Each step of the process involved sending the customer an email, meaning that a single order would usually result me in sending 5-6 emails to the customer over the course of the transaction. Considering the hundreds of customers we had to handle, this meant that I had to send quite a few emails.
</br> </br>
The process of sending an email started with going to the Google Doc which contained all of the email templates for each step in the e-commerce process. We would then have to copy the template and replace certain sections with the transaction specific information such as the customer's name and the order number. This, of course, became incredibly tedious over a long period of time. So, I decided to spend a day learning tkinter in Python to make a quick, easy, and terrible looking GUI to streamline the process.


## Getting Started
To download and use this script, follow these simple steps.

### Prerequisites
In order for the script to run (for now) you need to have the following text files in a folder named "texts" in the same directory as the script.
* `appletracking.txt`
* `invoice.txt`
* `lightspeednotes.txt`
* `order.txt`
* `quote.txt`
* `repairpayment.txt`
* `spss.txt`

You also need to have python3 installed along with tkinter (tkinter usually comes with python3). Go to [Python's website](https://www.python.org/downloads/) to install the latest version of Python if you don't have it and go to [tkinter's documentation](https://tkdocs.com/tutorial/install.html) to learn to how install tkinter.


### Installation
To download the script, download the zip file and extract it. Then follow the instructions below.

## Usage

### Executing the Script
There are different ways to execute the script depending on your operating system.

Windows:

1. Right-click `sales.py` and go to Security
2. Check Allow for the Read & Execute option 
3. Rename the file to "sales.pyw"
4. You can now simply double click on the script to run it.
5. For easier access, create a shortcut by right clicking `sales.pyw` and choosing "Create shortcut"

Mac:

1. Use a Terminal instance and the `ls` and `cd` commands to find the folder you downloaded.
2. Type `chmod +x sales.py` and press `Enter`.
2. Drag and drop `sales.py` into your Terminal.
3. Use your arrow keys to add `./` before sales.py so that it looks like this: `/./sales.py`
5. Save the path from your Terminal into a notepad. You can paste this command into any new Terminal in the future to run the program.

Linux:
	
1. Use a Terminal instance and use the `ls` and `cd` commands to find the folder you downloaded.
2. Type `chmod +x sales.py` and press `Enter`.
3. Rename `sales.py` to just `sales`
4. You can now simply double click on the script to run it.

### Using the GUI

The GUI has a small set of functions:

1. Enter your name (First name)
2. Choose between a list of options for emails to send.
4. Click on `Copy to Clipboard`. This will automatically copy the preview that shows up to your clipboard.
5. Clear the text and previous input.

## Road Map
I made this in a day, so I did not have the chance to implment many features that I had thought of. 

### Potential Features
* Change the files so that it can be made into an executable using pyinstall
* Create a built-in UI to edit the text files with the templates directly
* Create a built-in UI that can add new email templates and their own corresponding page

### Known Issues
* Extremely limited functionality
* Very ugly UI
* Simple UI provides a bad UX as it does not provide much convenience
