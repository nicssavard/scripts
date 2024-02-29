import os
import subprocess


def git_pull_execute(repo_dir, command):

    for service in services:

        # Change to the Git repository directory
        os.chdir(repo_dir + service)

        # Execute 'git pull' and capture the output
        try:
            pull_output = subprocess.check_output(
                ["git", "pull", "origin", "master"], text=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while pulling from Git: {e}")
            return

        print(pull_output)

        # Check if new changes were pulled
        if "Already up to date." in pull_output:
            print("No changes were pulled from the master branch.")
        else:
            print("New changes were pulled from the master branch.")
            # Execute the specified command
            try:
                subprocess.run(command, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"An error occurred while executing the command: {e}")


# Example usage
repo_dir = "/home/kali/jmap/"
services = ["jmapcloud-configuration-server", "jmapcloud-security",
            "jmapcloud-gateway", "jmapcloud-data-access",
            "jmapcloud-data-integration", "jmapcloud-extension",
            "jmapcloud-file-upload", "jmapcloud-map-configuration",
            "jmapcloud-map-image", "jmapcloud-process",
            "jmapcloud-vector-tile-cache"]

command = "./buildAndPush.sh dev-nsavard"  # Replace with your command
git_pull_execute(repo_dir, command)
