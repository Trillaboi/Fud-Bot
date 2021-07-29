const {Client} = require('discord.js');

const client = new Client();

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