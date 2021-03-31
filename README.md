# PasswordGenerator
A small password generator were you can choose how your password should look

This is a password generator in which you can choose the length of your password and also if your password has to include lower case, upper case, numbers and special
characters or punctuations. Each of the choosen things that has to be included are at least included in the final password once. The password is finaly created via
the secrets python module and not the random module since random in programming is not realy random. Secrets is using local factors of your own computer like microphone
noise or current fluctuations. This makes it only possible to predict if you use the same computer were the password was created
