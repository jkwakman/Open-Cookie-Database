## Introduction

This document aims to help contributors update the Open Cookie database. Contributors can add new cookies, update existing information, or ensure the correct categorization and descriptions of cookies.

The information gathering process aims to identify uncategorized cookies to support users and developers in gathering more information about the cookies set on their websites. The Open Cookie Database is an open-source database used by PSAT and other projects that maps cookies around the web, providing the following information: 
- **ID**: unique ID to identify the cookie
- **Platform**: Platform/Service responsible for setting the cookie 
- **Category**: Classification for the cookie's usage: Functional, Analytics, Marketing
- **Cookie Name**: Name from the respective cookie
- **Domain**: The domain in which the cookie is set; it can have a specific value or be empty when the cookie is set as the first party.
- **Description**: An introduction to the utility of the cookie  
- **Retention period**: The time when the cookie storage expires
- **Data Controlle**r: The company responsible for controlling the data
- **User Privacy & GDPR**: URL from the Privacy policy page or GDPR compliance
- **Wildcard**: A 0 in this column means that the cookie name is not a wildcard, and a 1 means that the cookie name is a wildcard

## Research
Contributing recently to the database, we recommend the following steps for collecting information about the cookie:

1. First, identify the cookie name and domain related to the cookie.
2. Use a search engine to find relative information about the cookie.
3. Use first queries to find information about the related domain, for example, site:example.com cookie-name. 
  a. In this case, the search will look for pages that contain references for the cookie name only in the described domain.
4. If you don’t find any information about it, on the previous search. Try to search by the specific name of the cookie, “cookie-name” with a double quote, and the domain used by the cookie. 
  a. As a result, the search engine will be more strict with results that only contain the cookie name.

If you find pages outside the company responsible for the cookie, double-check on more than one page to see if the description matches on more than one page. Review the information and double-check if the cookie wasn’t registered previously. 


## Categorization
Finding information about cookies is free for the person executing the audit. You will need to find the company responsible for the cookie, a category where this cookie fits, a description, and the retention period.

This information can be collected from more than one webpage. Pages like the Privacy policy, cookies policy, and developer documentation are the main sources of that information. We recommend looking first at the company's website responsible for cookies (Data Controller) and after partners who used the service or Cookiepedia. 

## Contributing to the repository
To contribute to the project, you will need a GitHub account for version control and a text editor like VS Code or a similar editor for the CSV file.

You can fork the GitHub project to start editing and creating your branches. Once you've filled in the information about the cookie, you'll be required to make a pull request to be evaluated by the repository owner. In the following section, we will explain step-by-step how you can set up the project.

## Setup repository on your local

Once you have your GitHub account, you must fork the Open Cookie Database repository. This step will create a repository with the same code and visibility in your account.

To fork, click on the fork button in the top-right corner of the upstream repository. 

Once your fork is ready, you must clone that repository to your computer. You can do this using the git command, or if you are not tech-savvy, you can use the GitHub application, which provides a GUI for ease of use.

We will discuss how you can  use the command line in the following process:

Open the terminal on Mac or PowerShell on Windows.
1. Enter the below command to clone the repository:
2. `$ git clone git@github.com:yourgithubname/Open-Cookie-Database.git`
3. Create a new branch from the master branch `$ git checkout -b cookie-vendor-name`
4. And now, you are ready to collaborate with the Open Cookie database
5. Open the file open-cookie-database.csv and start to contribute.

## Editing
Once you are ready, remember to create a branch, for example, `cookie-[vendor-name]` to submit your changes and start editing the file. The first information is a UUID to register the new cookie. A unique ID creates this information. You can find it online at websites like https://www.uuidgenerator.net/ or use the node package UUID: `$ npx uuid`. 

Add the related information to the cookie, and two fields could have special attention. The cookie name could have a dynamic ID, for example, `cookie_[site-id]`. If this applies to your case, the last property on the cookie is a wildcard. For wildcard cookies, set the value to 1 instead; the dynamic property doesn’t need to be specified. For example, we set the previous cookie as `cookie_`.

In another scenario, some solutions set the cookies as first-party; for this scenario, it can be empty.

## How to organize the cookies
Those steps are not a requirement but can help to organize the database.
When you add cookies from a platform already registered in the database, try to group them in the same group.
Cookies from the same platform can also be organized by product.

## Creating a pull request
After adding the new information, make sure to save the changes and start the process of submitting the changes:
Stage the changes from the open-cookie-database.csv by running:
$ git add  open-cookie-database.csv
After staging the changes, commit it by running:
$ git commit -am “The {X} number of cookies are added for {vendor}.” 
Once changes are committed, push the branch by running:
$ git push origin cookie-vendor-name