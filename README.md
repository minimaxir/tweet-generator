# Tweet Generator

![dank](/docs/textgenrnn_console.gif)

Train a neural network optimized for generating tweets based off of any number of Twitter users! Blend wildly different Twitter users together for hilarity!

Tweet Generator is based off of [textgenrnn](https://github.com/minimaxir/textgenrnn), and trains the network using context labels for better tweet synthesis.

## Usage

Open `config.yml` and at the top, add the Twitter API keys from a Twitter App you own. Then configure the list of `twitter_users` you wish to train the network on. You can also configure the `num_epochs` and whether to use the pretrained model or train a `new_model`. Then simply run:

```sh
python3 tweet_generator.py
```

The script will automatically save the weights (+ config and vocab for if `new_model`) for the trained model, which can then be loaded into textgenrnn and used anywhere.

The included `realDonaldTrump_dril_twitter_weights.hdf5` was trained on @[realDonaldTrump](https://twitter.com/realDonaldTrump) and @[dril](https://twitter.com/dril)'s tweets for 200 epochs. You can load it and generate text from it simply with:

```python
from textgenrnn import textgenrnn
textgen=textgenrnn('realDonaldTrump_dril_twitter_weights.hdf5')
textgen.generate_samples()
```

## Requirements

* textgenrnn
* tensorflow (either CPU or GPU flavors)
* tweepy

## Maintainer

Max Woolf ([@minimaxir](http://minimaxir.com))

*Max's open-source projects are supported by his [Patreon](https://www.patreon.com/minimaxir). If you found this project helpful, any monetary contributions to the Patreon are appreciated and will be put to good creative use.*

## License

MIT