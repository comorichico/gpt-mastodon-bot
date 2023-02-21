from mastodon import Mastodon

mastodon = Mastodon(access_token = 'gptchan_clientcred.txt')
mastodon.toot('テストツイートだよー')