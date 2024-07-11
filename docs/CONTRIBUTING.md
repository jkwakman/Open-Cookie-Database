## Introduction

This document guides contributors in updating the Open Cookie Database, an open-source project dedicated to identifying web cookies. Contributors can add new cookies, enhance existing information, and ensure accurate cookie categorization and descriptions.

Identifying web cookies is crucial for various research and open-source projects that rely on the Open Cookie Database. The database provides the following information:
- **ID**: unique ID to identify the cookie
- **Platform**: Platform/Service responsible for setting the cookie 
- **Category**: Classification for the cookie's usage: Functional, Analytics, Marketing
- **Cookie Name**: Name from the respective cookie
- **Domain**: The domain in which the cookie is set; it can have a specific value or be empty when the cookie is set as the first party.
- **Description**: An introduction to the utility of the cookie  
- **Retention period**: The time when the cookie storage expires
- **Data Controller**: The company responsible for controlling the data
- **User Privacy & GDPR**: URL from the Privacy policy page or GDPR compliance
- **Wildcard**: A 0 in this column means that the cookie name is not a wildcard, and a 1 means that the cookie name is a wildcard

## Research
The initial step is identifying cookies not listed in the database. Contributors can follow these steps to gather information about a cookie:

1. **Identify the cookie name and domain:** Begin by identifying the cookie's name and associated domain.
2. **Search for information:** Utilize a search engine to find relevant information about the cookie.
3. **Search within the domain:** Refine your search by using queries like `site:example.com "cookie-name"`. 
  a. In this case, the search will only list pages from the passed domain, that contain references for the exact cookie name.
4. **Broaden the search:** If no information is found, try searching using the cookie name within double quotes and specifying the domain, such as `"cookie-name" from example.com`. This will yield stricter results containing the cookie name, potentially across different domains.

If you find pages outside the company responsible for the cookie, double-check on more than one source to see if the description matches on more than one page. Review the information and finally double-check if the cookie wasn’t registered previously.

### Categorization
Finding information about cookies is free for the person executing the audit. You will need to find the company responsible for the cookie, a category where this cookie fits, a description, and the retention period. The accepted categories are:

1. Analytics
2. Functional
3. Marketing
4. Security
5. Personalization

This information can be collected from more than one webpage. Pages like the **Privacy Policy**, **Cookies Policy**, and developer documentation are the main sources of that information. We recommend looking first at the company's website responsible for cookies (Data Controller) and after partners who used the service or [Cookiepedia](https://cookiepedia.co.uk/).

### Organizing Cookies
Those steps are not a requirement but can help to organize the database.
When you add cookies from a platform already registered in the database, try to group them in the same group.
Cookies from the same platform can also be organized by product.

## Contributing to the repository
To contribute to the project, you will need a [GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) for version control and a text editor like [VS Code](https://code.visualstudio.com/) or a similar editor for the CSV file.

To improve the readability of the CSV file, some code editors, such as Visual Code, have extensions to provide a better visualization from the CSV file:

- [Edit CSV](https://marketplace.visualstudio.com/items?itemName=janisdd.vscode-edit-csv)
- [CSV rainbow](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)
- [CSV to table](https://marketplace.visualstudio.com/items?itemName=phplasma.csv-to-table)

You can fork the GitHub project to start editing and creating your branches. Once you've filled in the information about the cookie, you'll be required to make a pull request to be evaluated by the repository owner. In the following section, we will explain step-by-step how you can set up the project.

## Setup repository on your local
Once you have your GitHub account, you must fork the Open Cookie Database repository. This step will create a repository with the same code and visibility in your account.

To fork, click on the fork button in the top-right corner of the upstream repository.

<img src="https://i.ibb.co/XsdGHQ9/github-repo-open-cookie-db.png" alt="Open cookie database repository" width="640">

Once your fork is ready, you must clone that repository to your computer. You can do this using the git command, or if you are not tech-savvy, you can use the GitHub application, which provides a GUI for ease of use.

We will discuss how you can  use the command line in the following process:

Open the terminal on Mac or PowerShell on Windows.
1. Enter the below command to clone the repository:
2. `$ git clone git@github.com:yourgithubname/Open-Cookie-Database.git`

<img src="https://i.ibb.co/z8WGHCX/github-clone-repo-open-Cookie.png" alt="Clone repository on Github" width="640">

1. Create a new branch from the master branch `$ git checkout -b cookie-vendor-name`
2. And now, you are ready to collaborate with the Open Cookie database
3. Open the file open-cookie-database.csv and start to contribute.

## Editing
Once you are ready, remember to create a branch, for example, `cookie-[vendor-name]` to submit your changes and start editing the file. The first information is a UUID to register the new cookie. A unique ID creates this information. You can find it online at websites like [uuid generator](https://www.uuidgenerator.net/) or use the node package UUID: `$ npx uuid`. 

Add the related information to the cookie, and two fields could have special attention. The cookie name could have a dynamic ID, for example, `cookie_[site-id]`. If this applies to your case, the last property on the cookie is a wildcard. For wildcard cookies, set the value to 1 instead; the dynamic property doesn’t need to be specified. For example, we set the previous cookie as `cookie_`.

<img src="https://i.ibb.co/Nn63CmP/open-cookie-db-vscode.png" alt="Open Cookie database on VS Code" width="640">

In another scenario, some solutions set the cookies as first-party; for this scenario, it can be empty.

## Creating a pull request
After adding the new information, make sure to save the changes and start the process of submitting the changes:
1. Stage the changes from the open-cookie-database.csv by running:
 `$ git add  open-cookie-database.csv`

2. After staging the changes, commit it by running:
`$ git commit -am “The {X} number of cookies are added for {vendor}.” `

3. Once changes are committed, push the branch by running:
 `$ git push origin cookie-vendor-name`

 Once the changes are pushed to a remote branch on GitHub, you are ready to create a pull request. Go to your GitHub account and create a New pull request as in the image below:

<img src="https://i.ibb.co/4gCJwMQ/create-pr-open-cookie-database.png" alt="create-pr-open-cookie-database" width="640">

 Set In the description of your pull request to the repository, you can use the following templates:

```
** Description **

This pull request contains [x] cookies from [company name] 

[company introduction if it was never listed on the cookie database]


** Source **

[list the links that you used to register the data]
```

Add the details to the description and click on the create pull request button. Your pull request will be created.

Once your pull request is created, the author of the upstream repo will review it. Once they are reviewed, he will approve and merge them. 

## Updating your local repo

When the pull request is merged or if there are any new changes in the upstream repo, you will need to update your repo on GitHub and your clone on the computer.

First, visit your forked repo and click on the **“Sync Fork”** button to keep your GitHub repo updated upstream. 

Secondly, open your clone in a terminal and run the `git checkout master` and `git pull origin master` commands. Your local repo will be updated with the latest changes. 
