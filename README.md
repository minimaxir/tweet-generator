# Tweet Generator

Train a neural network optimized for generating tweets based off of any number of Twitter users! Blend wildly different Twitter users together for hilarity!

Tweet Generator is based off of textgenrnn, and trains the network using context labels for easier tweet synthesis.

## Usage

Open `config.yml` and at the top, input the list of `twitter_users` you wish to train the network on. You can also configure the `num_epochs` and whether to use the pretrained model or train a `new_model`. At the bottom of the file, add the Twitter API keys from a Twitter App you own. Then simply run:

```sh
python3 tweet_generator.py
```

The script will automatically save the weights (+ config and vocab for if `new_model`) for the trained model, which can then be reloaded into textgenrnn and used anywhere.

## Requirements

* textgenrnn
* tensorflow (either CPU or GPU flavors)
* tweepy

## Maintainer

Max Woolf ([@minimaxir](http://minimaxir.com))

*Max's open-source projects are supported by his [Patreon](https://www.patreon.com/minimaxir). If you found this project helpful, any monetary contributions to the Patreon are appreciated and will be put to good creative use.*

## License

MIT

Code used from Mask R-CNN by Matterport, Inc. (MIT-Licensed), with minor alterations and copyright notices retained.