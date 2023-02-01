
# Sicarius


![/static/banner.png](/static/f.png)

<h4 align="center">  🐴 ⚡️ Fast subdomain enumeration tool 🐴 ⚡️</h4>
<a href="https://twitter.com/unp4ck">🦆 @unp4ck</a>
<p> Version 1.1.2 Codename Edwin (😅 BETA!) <p>

![alt text](https://img.shields.io/github/stars/unp4ck/Sicarius)
![alt text](https://img.shields.io/github/languages/top/unp4ck/Sicarius)
![alt text](https://img.shields.io/github/license/unp4ck/Sicarius)


### Install

🚨 !! Only if you need extract method !! 🚨
<br>
🚨 Note, the first time you ever run the render() method, it will download Chromium into your home directory (e.g. ~/.pyppeteer/). This only happens once. You may also need to install a few Linux packages to get pyppeteer working. https://github.com/miyakogi/pyppeteer/issues/60 🚨



```bash

git clone github.com/unp4ck/sicarius.git

cd sicarius

touch config/config.yaml

# add your apis keys here!

pip3 install -r requirements.txt --user
```

### Post Installation

API Key is needed before querying on third-party sites;

##### Sicarius have 12 Sources to grab subdomains.

* ```Shodan``` 
* ```SecurityTrails```
* ```Virustotal``` 
* ```BinaryEdge```
* ```chaos``` - [https://chaos.projectdiscovery.io/#/docs](https://chaos.projectdiscovery.io/#/docs)
* ```ctrsh```
* ```wayback```
* ```threatcrowd```
* ```certspooter```
* ```hackertarget```
* ```urlscan```
* ```alienvault```

- **The API key setting can be done via `config.yaml`**

An example provider config file 

```yaml
virustotal:
  - XXXXXXXXXXXXXXX
securitytrails: []
shodan:
  - XXXXXXXXXXXXXXXXXXX
```

### Usage



```bash

usage: sicarius.py [-h] [-d DOMAIN] [-e] [-l DOMAINLIST] [-sc] [-title] [--scope SCOPE] [-t THREADS] [-ip] [-v] [-silent] [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        domains to find subdomains for
  -e, --extract (working progress )         Extract: links ( inside JS to ), headers, useful for new domains and second order subdomain takeover
  -l DOMAINLIST         file containing list of domains for subdomain discovery
  -sc, --status-code    show response status code
  -title, --title       show page title
  --scope SCOPE         show only subdomains in scope
  -t THREADS, --threads THREADS
                        number of concurrent threads for resolving (default 40)
  -ip, --ip             Resolve IP address
  -v                    show verbose output
  -silent, --silent     show only subdomains in output
  -o OUTPUT, --output OUTPUT
                        file to write output to
```

### Running Sicarius
```bash
cat domains | python3 sicarius.py
```

```bash
### probe subdomains collected (like httpx, httprobe..)

cat domains | python3 sicarius.py -sc

```

```bash
## probe and resolve IP 
cat domains | python3 sicarius.py -sc -ip
```

### You can pipe with other tools like nuclei, httpx etc..

```bash
# httpx to probe
echo intigriti.com | python3 sicarius.py -silent | httpx -silent 
# pipe to nuclei
echo intigriti.com | python3 sicarius.py -silent | httpx -silent | nuclei -t <path_to_nuclei_templates>

```

```bash

# running and probing and extract all absolute links, saving the results at h1_links and the domains at h1 folder ( WE NEED -sc flag! )
python3 sicarius.py -d hackerone.com -e -eo h1_links -o h1 -sc


```

```bash
python3 sicarius.py -d intigriti.com


	░██████╗██╗░█████╗░░█████╗░██████╗░██╗██╗░░░██╗░██████╗
	██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║██║░░░██║██╔════╝
	╚█████╗░██║██║░░╚═╝███████║██████╔╝██║██║░░░██║╚█████╗░
	░╚═══██╗██║██║░░██╗██╔══██║██╔══██╗██║██║░░░██║░╚═══██╗
	██████╔╝██║╚█████╔╝██║░░██║██║░░██║██║╚██████╔╝██████╔╝
	╚═════╝░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░╚═════╝░╚═════╝░

	    -= ⚡️ Fast subdomain enumeration tool ⚡️ =-


	 [Version: 1.0.1 Codename: Edwin ♥️ [author: unp4ck][tw: @unp4ck]]

[20:14:32] [ 🔎]: certspotter.com 5 domains founded! ✅
[20:14:32] [ 🔎]: securitytrails.com 30 domains founded! ✅
[20:14:32] [ 🔎]: securitytrails.com 54 domains founded! ✅
[20:14:32] [ 🔎]: urlscan.io 52 domains founded! ✅
[20:14:33] [ 🔎]: alienvault.com 136 domains founded! ✅
[20:14:33] [ 🔎]: hackertarget.com 10 domains founded! ✅
[20:14:33] [ 🔎]: binaryedge.io 8 domains founded! ✅
[20:14:33] [ 🔎]: virustotal 46 domains founded! ✅
[20:14:34] [ 🔎]: wayback 8696 assets founded! ✅
[20:14:40] [ 🔎]: crt.sh 251 domains founded! ✅

[20:14:41] [INF]: Found 58 for intigriti.com

www.intigriti.com
mail.intigriti.com
login.intigriti.com
app.intigriti.com
newsletter.intigriti.com
api.intigriti.com
blog.intigriti.com
kb.intigriti.com
communication.intigriti.com
go.intigriti.com
hello.intigriti.com
careers.intigriti.com
swag.intigriti.com
click-uat.intigriti.com
t.intigriti.com
trust.intigriti.com


```

### Congrats/thanks
   - Thanks [duty1g](https://github.com/duty1g) ~ [subcat](https://github.com/duty1g/subcat) 🖤


### Features


* Absolute links collector, even with Javascript only pages!! ✨ 
![/static/sc.gif](/static/edwin.gif)
![/static/sc.gif](/static/edwin_links.png)


* Only subdomains using passove apis

![/static/sc.gif](/static/yuo.gif)


- Modular,fast,lightweigth 🍦 
- Wildcard elimination module 🙅🏽‍♂️ 
- Scope limitation based on given IP ranges list 📸 
- Extracts links and headers, for second order subdomain takeveover or new subs ✨ 🥷 ✨  -> | **Warning: the first time you run this method, it will download Chromium into your home directory (~/.pyppeteer)** ( render Javascript ;) ) ( BETA !)

#### Meaning of sicarius

```
Sicarius is a genus of recluse spiders that is potentially medically significant to humans. It is one of three genera in its family, all venomous spiders known for a bite that can induce loxoscelism. They live in deserts and arid regions of the Neotropics, and females use a mixture of sand and silk when producing egg sacs. The name is Latin for assassin.
```
