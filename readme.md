# Discogs Command Line Sellers Tool

## Usage

Using your Discogs account, get info on a list of vinyl, including a helpful price range for what to sell the items for, the number of the same vinyl already for sale, and some metadata on each vinyl release

## Setup

Navigate to Discogs and get your account setup as a [Seller](https://www.discogs.com/settings/seller/). Once that's completed, navigate to the [Developer](https://www.discogs.com/settings/developers) window and generate a new `personal access token` Assign that to the `token` field in the config file.

There are two different ways to get the vinyl IDs for the program

#### Folder method (-f)

Create a folder in discogs, and add the vinyl to that folder. Once there, look in the URL for the id (`folder={MY_ID}`) and assign _folder_ to that id in the config file. You will also need to input your _username_ in the config file as well.

#### Filepath method (-p)

If you have the IDs in a txt file, you can also add the absolute path to your txt file in the _filepath_ field (i.e. `C://my_path/file.txt`).

## Running the program

Navigate to the `discogs_vinyl_sellers_tool` directory using your preferred terminal. Once there, input `python main.py` follwed by either `-f` or `-p` depending on if you want to use the folder option or filepath option respectively. Press enter and the program should output your vinyl data!