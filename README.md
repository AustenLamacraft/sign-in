On MWS I use the following `.htaccess`

```
AddHandler wsgi-script .wsgi

Options FollowSymlinks ExecCGI MultiViews Indexes
MultiviewsMatch Handlers

RewriteEngine on
RewriteBase /
RewriteRule ^(signin(/)?)$  /signin/signin.wsgi  [L,QSA]
```
