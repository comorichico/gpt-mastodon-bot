from mastodon import Mastodon
# urlとログインに使うメールアドレス、パスワードを
# 自分の設定に置き換えてください。
# cred_file_nameとapp_nameはそのままでも変えてもいいです。
# cred_file_nameを変えた場合はgpt.pyも同じ個所を変えてください。
mastodon_url = 'https://mastodon.comorichico.com/'
mastodon_login_mail = 'mastodon@comorichico.com'
mastodon_login_password = 'password'
cred_file_name = 'gptchan_clientcred.txt'
app_name = 'GPTちゃん'

Mastodon.create_app(
    app_name,
    api_base_url = mastodon_url,
    to_file = cred_file_name
)

mastodon = Mastodon(client_id = cred_file_name,)
mastodon.log_in(
    mastodon_login_mail,
    mastodon_login_password,
    to_file = cred_file_name
)