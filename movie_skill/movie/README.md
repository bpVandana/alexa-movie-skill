# Alexa movie skills

## Introduction

This is an alexa skill which suggests movies  when you ask for it. It can also be used a a boilerplate for building alexa skills.

## How does it work?

### Workflow
You can test out this skill using an Amazon Echo device or at [Echosim](https://echosim.io). The workflow is as follows:
- You invoke the skill saying "Alexa, suggest me a movie."
- Alexa will suggest you moovies ..
- If you say yes, it would again give you a next movie  . If you say no, it will exit out of the skiil.

### Internal Implementation

This skill is written in Python using Flask and the python library [Flask-Ask](https://github.com/johnwheeler/flask-ask). The Implementation is as follows:
- When you invoke the skill, one of the Yoda quotes is fetched from the database (this data comes along with this project. Don't worry about adding it yourself)and spoken out by Alexa along with a question if you want more of yoda quotes.
- If you say yes, first step repeats.
- If you say no, Alexa echoes "Bye" and exits out of the skill.

## How to get it up and running?

### Deployment
This skill gets deployed instantly. Also, Hasura automatically generates SSL certificates for you. Just run the following commands to deploy your skill.

(Make sure you have [hasura-cli](https://docs.hasura.io/0.15/manual/install-hasura-cli.html))

```
$ hasura quickstart bpvandana/alexa_movie_skill
$ cd alexa-yoda-bot
$ git add . && git commit -m "Initial Commit"
$ git push hasura master
```

### How to add the skill to your Amazon account?

To link it with your Amazon Echo Device, go to your [Amazon developer console](https://developer.amazon.com/edw/home.html#/skills).

1. Create a new skill. Call it `Suggest Movie`. Give the invocation name as `suggest movie`. Click next.

2. Add this intent schema
```
{
  "intents": [
    {
      "intent": "YesIntent"
    },
    {
      "intent": "NoIntent"
    },
    {
      "intent": "suggestMovie"
    }
  ]
}
```

Leave custom slot types empty. Add the following sample utterances

```
YesIntent yes
YesIntent sure
YesIntent yeah
YesIntent ok
NoIntent no
NoIntent no thanks
NoIntent nope
suggestMovie suggest a movie
suggestMovie suggest me a movie
```

   Click next.

3. For the service endpoint, check the `HTTPS` radio button.

	Put the default URL as `https://bot.<cluster-name>.hasura-app.io/movies`. (Run `$ hasura cluster status` from root directory to know your cluster name).

	**Note**: For quick testing, we have one skill service live at https://bot.incipiently69.hasura-app.io/movie(This test service will work only if you have followed 1 and 2)

	Click next.

4. About SSL certificates, Hasura services have auto generated `LetsEncrypt` Grade A SSL certificates. This means, you have to check the radio button that says `My development endpoint has a certificate from a trusted certificate authority`

	Click next.

5. Your skill is live on the ECHO device associated with your account. Test it by saying **Alexa**, `suggest a movie`. And Alexa will give you movies

## How to use it as a boilerplate?

The source code lies in the `microservices/bot/app/src` directory. This is a simple application, so the entire code lies in `server.py`.

You might want to go through the Flask-ask docs (a very quick read).

## Support

If you happen to getstuck at any point, feel free to mail me at vandanakumari291@gmail.com. Also, if you find an error or a bug, please raise an issue [here](https://github.com/bpvandana/alexa-movie-skill).
