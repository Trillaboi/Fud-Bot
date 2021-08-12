const {Client} = require('discord.js');
const {spawn} = require('child_process');

const tweepy = spawn('python3', ["-u", "python_scripts/tweets.py"], {stdio:['ipc', 'pipe', 'pipe']})

const client = new Client();

tweepy.stdout.setEncoding('utf-8')
tweepy.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
})

tweepy.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
})

tweepy.on('exit', (code, error) => {
    console.log(`tweepy proccess exited with code ${code}`);
})

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', message => {
    if (!message.author.bot)
        console.log(message.content);
    if (message.content === 'ping') {
        message.channel.send('pong');
    } 
});

client.login('ODcwMzI1Mzg4MjQ3Njk5NDc4.YQLHrg.kKA6L_-sHKMRS3yNqgqMcFtIfZc')