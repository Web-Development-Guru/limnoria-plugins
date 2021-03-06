# SpiffyTitles #

The ONLY gluten-free plugin for displaying link titles.

## Requirements ##

- This plugin requires Python 2.7. It might work in other versions, though.
- If you need to install `certifi` you may have to restart the bot afterwards

## Notable features ##

- Configurable template so you can decide how titles are displayed and what they say
- Additional information about [Youtube](https://youtube.com) videos
- Additional information about [imgur](https://imgur.com) links
- Rate limiting to mitigate abuse
- Configurable white/black list to control where titles are disabled
- Configurable list of user agents
- Ability to ignore domains using a regular expression

Check out the [available options](#available-options)

## Using SpiffyTitles ##
- `git clone https://github.com/prgmrbill/limnoria-plugins.git`
- `cd limnoria-plugins/SpiffyTitles`
- Install the requirements: `pip install -r requirements.txt --user --upgrade`
- You should `unload` the Web plugin and any other plugins that show link titles for best results

To unload the Web plugin:

    !unload Web

Load SpiffyTitles:
    
    !load SpiffyTitles

Tip: Observe the logs when loading the plugin and afterwards to see what's going on under the hood.

## Available Options ##

### Default handler ###

`defaultHandlerEnabled` - Whether to show additional information about links that aren't handled elsewhere. You'd really only 
want to disable this if all of the other handlers were enabled. In this scenario, the bot would only show information for
websites with custom handlers, like Youtube, IMDB, and imgur.

`defaultTitleTemplate` - This is the template used when showing the title of a link. 

Default value: `^ {{title}}`

Example output:

    ^ Google.com

### Youtube handler

Note: as of April 20 2015 version 2 of the Youtube API was deprecated. As a result, this feature now
requires a [developer key](https://code.google.com/apis/youtube/dashboard/gwt/index.html#settings).

- Obtain a [developer key](https://code.google.com/apis/youtube/dashboard/gwt/index.html#settings)
- Go to the `Credentials` area, choose `Public API access` and `Create new Key` as shown in the screenshot below

![Google Developer Console Screenshot](https://i.imgur.com/IUfk3VB.jpg "Google Developer Console Screenshot")

- You may specify allowed IPs but be aware that this setting seems to cache. It is easier to test using the URL listed in the console to verify requests from that machine are working.
- Make sure the YouTube API is enabled in [the developer console](https://developers.google.com/console/help/#activatingapis).
- Set the key: `!config supybot.plugins.SpiffyTitles.youtubeDeveloperKey your_developer_key_here`
- Reload: `!reload SpiffyTitles`
- Observe the logs to check for errors

### Youtube handler options

`youtubeHandlerEnabled` - Whether to show additional information about Youtube links

`youtubeTitleTemplate` - This is the template used when showing the title of a YouTube video

Default value: `^ {{title}} uploaded by {{channel_title}} :: Duration: {{duration}} :: {{view_count}} views :: {{like_count}} likes :: {{dislike_count}} dislikes :: {{favorite_count}} favorites :: {{comment_count}} comments`

Example output:

    ^ Snoop Dogg - Pump Pump feat. Lil Malik uploaded by GeorgeRDR3218 :: Duration: 04:41 :: 203,218 views :: 933 likes :: 40 dislikes :: 0 favorites :: 112 comments

Tip: after changing a template, you must `!reload SpiffyTitles`

### imdb handler ###
Queries the [OMDB API](http://www.omdbapi.com) to get additional information about [IMDB](http://imdb.com) links

`imdbHandlerEnabled` - Whether to show additional information about [IMDB](http://imdb.com) links

`imdbTemplate` - This is the template used for [IMDB](http://imdb.com) links

Default value: `^ {{Title}} ({{Year}}, {{Country}}) - Rating: {{imdbRating}} ::  {{Plot}}`

### imgur handler ###

`imgurTemplate` - This is the template used when showing information about an [imgur](https://imgur.com) link.

Default value

    ^ {%if section %} [{{section}}] {% endif -%}{%- if title -%} {{title}} :: {% endif %}{{type}} {{width}}x{{height}} {{file_size}} :: {{view_count}} views :: {%if nsfw == None %}not sure if safe for work{% elif nsfw == True %}not safe for work!{% else %}safe for work{% endif %}

Example output:

    ^ [pics] He really knows nothing... :: image/jpeg 700x1575 178.8KiB :: 809 views :: safe for work

`imgurAlbumTemplate` - This is the template used when showing information about an imgur album link.

Default value

    ^ {%if section %} [{{section}}] {% endif -%}{%- if title -%} {{title}} :: {% endif %}{{image_count}} images :: {{view_count}} views :: {%if nsfw == None %}not sure if safe for work{% elif nsfw == True %}not safe for work!{% else %}safe for work{% endif %}

Example output:
    
    ^ [compsci] Regex Fractals :: 33 images :: 21,453 views :: safe for work

### Using the imgur handler ###

- You'll need to [register an application with imgur](https://api.imgur.com/oauth2/addclient)
- Select "OAuth 2 authorization without a callback URL"
- Once registered, set your client id and client secret and reload SpiffyTitles

    `!config supybot.plugins.SpiffyTitles.imgurClientID`
    
    `!config supybot.plugins.SpiffyTitles.imgurClientSecret`
    
    `!reload SpiffyTitles`

### Notes on the imgur handler ###

- If there is a problem reaching the API the default handler will be used as a fallback. See logs for details.
- The API seems to report information on the originally uploaded image and not other formats
- If you see something from [the imgur api](https://api.imgur.com/models/image) that you want and is not available
in the above example, [please open an issue!](https://github.com/prgmrbill/limnoria-plugins/issues/new)

`useBold` - Whether to bold the title. Default value: `False`

`linkCacheLifetimeInSeconds` - Caches the title of links. This is useful for reducing API usage and 
improving performance. Default value: `60`

`wallClockTimeoutInSeconds` - Timeout for total elapsed time when retrieving a title. If you set this value too 
high, the bot may time out. Default value: `8` (seconds). You must `!reload SpiffyTitles` for this setting to take effect.

`channelWhitelist` - a comma separated list of channels in which titles should be displayed. If `""`,
titles will be shown in all channels. Default value: `""`

`channelBlacklist` - a comma separated list of channels in which titles should never be displayed. If `""`,
titles will be shown in all channels. Default value: `""`

### About white/black lists ###

- If `channelWhitelist` and `channelBlacklist` are empty, then titles will be displayed in every channel
- If `channelBlacklist` has #foo, then titles will be displayed in every channel except #foo
- If `channelWhitelist` has #foo then `channelBlacklist` will be ignored

### Examples ###

### Show titles in every channel except #foo ###

    !config supybot.plugins.SpiffyTitles.channelBlacklist #foo

### Only show titles in #bar ###

    !config supybot.plugins.SpiffyTitles.channelWhitelist #bar

### Only show titles in #baz and #bar ###

    !config supybot.plugins.SpiffyTitles.channelWhitelist #baz,#bar

### Remove channel whitelist ###
    
    !config supybot.plugins.SpiffyTitles.channelWhitelist ""

`ignoredDomainPattern` - ignore domains matching this pattern. Default value: `""`

`whitelistDomainPattern` - ignore any link without a domain matching this pattern. Default value: `""`

### Tip ###

You can ignore domains that you know aren't websites. This prevents a request from being made at all.

### Examples ###

Ignore all links with the domain `buzzfeed.com`

    !config supybot.plugins.SpiffyTitles.ignoredDomainPattern (buzzfeed\.com)

Ignore `*.tk` and `buzzfeed.com`

    !config supybot.plugins.SpiffyTitles.ignoredDomainPattern (\.tk|buzzfeed\.com)

Ignore all links except youtube, imgur, and reddit

    !config supybot.plugins.SpiffyTitles.whitelistDomainPattern /(reddit\.com|youtube\.com|youtu\.be|imgur\.com)/

`userAgents` - A comma separated list of strings of user agents randomly chosen when requesting. 

`urlRegularExpression` - A regular expression used to match URLs. You shouldn't need to change this.

### FAQ ###

Q: How can I only show information about certain links?

A: You can use the settings `defaultHandlerEnabled`, `youtubeHandlerEnabled`, `imgurHandlerEnabled`, and `imdbHandlerEnabled` to choose which links you want to show information about. You must also `!reload SpiffyTitles` after changing these settings.

Q: Why not use the [Web](https://github.com/ProgVal/Limnoria/tree/master/plugins/Web) plugin?

A: My experience was that it didn't work very well and lacked the ability to customize the options
I wanted to change.

Q: What about [Supybot-Titler](https://github.com/reticulatingspline/Supybot-Titler) ?

A: I couldn't get this to work on my system and it has a lot of features I didn't want

Q: It doesn't work for me. What can I do?

A: [Open an issue](https://github.com/prgmrbill/limnoria-plugins/issues/new) and include at minimum the following:

- Brief description of the problem
- Any errors that were logged (Look for the ones prefixed "SpiffyTitles")
- How to reproduce the effect
- Any other information you think would be helpful
