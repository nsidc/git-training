# About SSH keys

Git hosting providers like GitHub and Bitbucket [used to allow HTTPS
username/password authentication](https://github.blog/changelog/2021-08-12-git-password-authentication-is-shutting-down/),
but have since disabled this feature security reasons. This is a good thing!
But this is a _very_ recent change as of this writing, so if you've used Git
before, you may be surprised at the need to use a different authentication
method.

We recommend configuring SSH keys with your Git hosting provider of choice for
authentication.


## Why SSH?

There are alternative methods to authenticate your `git` client with GitHub and
Bitbucket, such as "Application Passwords", "Personal Access Tokens", or
browser-based authentication with tools like GitHub CLI. For simplicity, these
training materials will focus on SSH because it is a fairly uniform user
experience on all providers and is a well-known convention.


## A warning about shared users

An SSH private key is _private_ and should be guarded like a password. If you
wouldn't save your password somewhere, you should also not save your SSH
private key there.


## What if I already have SSH keys?

It is valid to use the same SSH key to authenticate with multiple providers, as
long as the private key (without `.pub` file extension) is not shared. You can
also create multiple SSH keys, but you will need to learn to manage those keys.

There are several ways to manage multiple SSH keys, but that is out of scope
for this training. Here are some external resources:

* [Managing keys with SSH Agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent)
* [Managing keys with SSH config file](https://stackoverflow.com/questions/3225862/multiple-github-accounts-ssh-config)


## How do SSH keys work?

This is out of scope for this training, but you can learn more here:

* [SSH Essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
