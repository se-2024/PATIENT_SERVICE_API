<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/se-2024/PATIENT_SERVICE_API">
    <img src="images/logo.png" alt="Logo">
  </a>

<h3 align="center">PATIENT_SERVICE_API</h3>

  <p align="center">
    This is a patient service api that will save and retrieve patient details. 
    <br />
    <a href="https://github.com/se-2024/PATIENT_SERVICE_API/blob/main/docs/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/se-2024/PATIENT_SERVICE_API/issues">Report Bug</a>
    ·
    <a href="https://github.com/se-2024/PATIENT_SERVICE_API/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This is a Python-based RESTful API that is part of the Hospital Management System.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* [![FastAPI][FastAPI]][FastAPI-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

Setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Required software and how to install them.
* python
  - MacOS: follow this guide - https://docs.python-guide.org/starting/install3/osx/ 

### Installation

- New repository setup
  1. Fork the Project (from the github website)
  2. Clone the forked repo locally
      ```sh
          git clone git@github.com:YOUR_USERNAME/PATIENT_SERVICE_API.git
      ```
  3. List the current configured remote repository for your fork. It should show only the forked version of the repository that you have just forked.
    ```sh
      $ git remote -v
        > origin  git@github.com:YOUR_USERNAME/PATIENT_SERVICE_API.git (fetch)
        > origin  git@github.com:YOUR_USERNAME/PATIENT_SERVICE_API.git (push)
    ```
  4. Specify a new remote upstream repository that will be synced with the fork.
    ***NOTE***: This will be the original owner - the se-2024/PATIENT_SERVICE_API repo:
    `git remote add upstream  https://github.com/se-2024/PATIENT_SERVICE_API.git`

  5. List out the remotes and this time you will have another remote:
    ```sh
      $ git remote -v
        origin	git@github.com:fbatroni/PATIENT_SERVICE_API.git (fetch)
        origin	git@github.com:fbatroni/PATIENT_SERVICE_API.git (push)
        upstream	git@github.com:se-2024/PATIENT_SERVICE_API.git (fetch)
        upstream	git@github.com:se-2024/PATIENT_SERVICE_API.git (push)
    ```
  
- Existing repository setup   <br/>
  ***NOTE***: You already have a PATIENT_SERVICE_API repo and you'd like to reset your existing repo to mirror the se-2024/PATIENT_SERVICE_API repo. These steps will result in resetting the existing code and ***any changes will be lost***.
  1. List the current configured remote repository for your repo. You should only have one that points to your repository hosted under your github username.
    ```sh
    $ git remote -v
      > origin  git@github.com:YOUR_USERNAME/PATIENT_SERVICE_API.git (fetch)
      > origin  git@github.com:YOUR_USERNAME/PATIENT_SERVICE_API.git (push)
    ```
    If you have another remote you can delete it. The only other remote you will need will be the upstream to the shared repository.
  2. Specify a new remote upstream repository that will be synced with your repo.
    ***NOTE***: This will be the original owner - the se-2024/PATIENT_SERVICE_API repo:
    `git remote add upstream  https://github.com/se-2024/PATIENT_SERVICE_API.git`

  3. List out the remotes and this time you will have another remote:
    ```sh
      $ git remote -v
        origin	git@github.com:fbatroni/PATIENT_SERVICE_API.git (fetch)
        origin	git@github.com:fbatroni/PATIENT_SERVICE_API.git (push)
        upstream	git@github.com:se-2024/PATIENT_SERVICE_API.git (fetch)
        upstream	git@github.com:se-2024/PATIENT_SERVICE_API.git (push)
    ```
  4. Reset your local main branch to match the remote upstream
    `git reset --hard upstream/main`

  5. Force push these changes to your repository so that all code is mirrored. This is a one-time operation.
    `git push origin main -f`
    ```sh
      Enumerating objects: 27, done.
      Counting objects: 100% (27/27), done.
      Delta compression using up to 8 threads
      Compressing objects: 100% (21/21), done.
      Writing objects: 100% (27/27), 144.44 KiB | 10.32 MiB/s, done.
      Total 27 (delta 0), reused 2 (delta 0), pack-reused 0
      To github.com:fbatroni/PATIENT_SERVICE_API.git
      + e0fc073...0be4789 main -> main (forced update)
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Testing
### Unit and Integration Testing
[pytest framework](https://docs.pytest.org/en/7.1.x/getting-started.html) - a Python testing framework that can be used to write various types of software tests, including unit tests, integration tests, end-to-end tests, and functional tests
[pytest-sqlalchemy-mock](https://github.com/resulyrt93/pytest-sqlalchemy-mock) - pytest fixtures to create an in-memory DB instance on tests and dump your raw test data
<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

(Assuming you've followed the steps in "Installation" section):
1. Fetch the latest from the upstream repository
  `git fetch upstream`
  ```sh
  remote: Enumerating objects: 27, done.
  remote: Counting objects: 100% (27/27), done.
  remote: Compressing objects: 100% (21/21), done.
  remote: Total 27 (delta 0), reused 27 (delta 0), pack-reused 0
  Unpacking objects: 100% (27/27), 144.42 KiB | 1.60 MiB/s, done.
  From github.com:se-2024/PATIENT_SERVICE_API
  * [new branch]      main       -> upstream/main
  ```
2. Check out your fork's local default branch - in this case, we use main. 
3. Merge the latest code from the upstream main branch into your local main
  `git merge upstream/main`
4. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
5. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
6. Push to the Branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/se-2024/PATIENT_SERVICE_API.svg?style=for-the-badge
[contributors-url]: https://github.com/se-2024/PATIENT_SERVICE_API/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/se-2024/PATIENT_SERVICE_API.svg?style=for-the-badge
[forks-url]: https://github.com/se-2024/PATIENT_SERVICE_API/network/members
[issues-shield]: https://img.shields.io/github/issues/se-2024/PATIENT_SERVICE_API.svg?style=for-the-badge
[issues-url]: https://github.com/se-2024/PATIENT_SERVICE_API/issues
[product-screenshot]: images/screenshot.png
[FastAPI]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[FastAPI-url]: https://fastapi.tiangolo.com/

