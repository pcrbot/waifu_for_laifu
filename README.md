# waifu_for_laifu

a wife generator based on waifu labs and laifu with waifu simulation game


## WIP warning

This project is still work in progress, not ready for production

## Usage

1. clone to somewhere
2. install dependencies `pip install -r requirements.txt`
3. make a soft link for inner module folder to nonebot/nb2/hoshino modules directory

for Windows: `D:\chatbot\modules>mklink /J waifu_for_laifu D:\waifu_for_laifu\waifu_for_laifu`

for Unix: `ln -s ./waifu_for_laifu/waifu_for_laifu waifu_for_laifu`

### Testing

run `python -m unittest`

## TODO

### functions

* √ generate a waifu with different poses
* randomly reply stored poses
* generate waifu parameters
* simple interactions using poses

### compatibility

* √ nonebot2a7-
* nonebot2a8+
* hoshino
* √ nonebot1

## Thanks

This module is inspired by [Waifu Labs](https://waifulabs.com/) which is made by Sizigi Studios and calls its api to generate a new waifu. Please consider supporting them on Patreon or Ko-fi to keep this service available.

Also the API is subject to change after April according to service provider on discord:

> Cixelyn
>
> there are no keys for this current version. We do ask you that you please limit your requests rate though; please try to stay under 1 request per second for now; let me know if you need something higher
> 
>just as a heads up: the API will probably change in April or so when we (finally) finish up and launch Waifulabs v2

Generated menu is inspired by [da_lao_jiu_gong_ge](https://github.com/pcrbot/da_lao_jiu_gong_ge) which is made by dalao H-K-Y
