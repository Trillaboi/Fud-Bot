const {Client} = require('discord.js');
const {spawn} = require('child_process');
const EventEmitter  = require('events');

const tweepy = spawn('python3', ["-u", "python_scripts/tweets.py"], {stdio:['ipc', 'pipe', 'pipe']})
const client = new Client();
const messageEmitter = new EventEmitter();

client.login('ODcwMzI1Mzg4MjQ3Njk5NDc4.YQLHrg.kKA6L_-sHKMRS3yNqgqMcFtIfZc')



// tweepy.stdout.setEncoding('utf-8')
tweepy.stdout.on('data', (data) => {
    try{
        command = JSON.parse(data);
        messageEmitter.emit('command', command);
        // console.log(`message sent: ${command}`);
    }catch(err){
        // When your sending frequent requests to connect a 420 error is sent but it doesnt usually affect anything.
        if(data !== 420)
        {
        console.log(err);
        console.log(`stdout: ${data}`);
        }
    }
    
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

// client.on('message', message => {
//     if (!message.author.bot)
//         console.log(message.content);
//     if (message.content === 'ping') {
//         message.channel.send('pong');
//     } 
// });

messageEmitter.on('command', (command) => {
    messageHandler(command);
})

function messageHandler(command)
{
    const newsChannel = client.channels.cache.get('870393495809065000')
    const whaleChannel = client.channels.cache.get('875797275815837708')
    const listingChannel = client.channels.cache.get('875489972008943636')
    const generalChannel = client.channels.cache.get('875492148131299368')
    const binanceChannel = client.channels.cache.get('875489972008943636')
    const ftxChannel = client.channels.cache.get('875492019114487859')
    const exchangeChannel = client.channels.cache.get('876135096997007381')

    formattedMsg = `From: @${command['user']}\n${command['text']}\nLink: `
    type = command['type']

    if(type == 'news')
    {
        newsChannel.send(formattedMsg)
    }
    else if (type == 'exchange'){
        if (command['exchange'] == 'ftx')
            ftxChannel.send(formattedMsg)
        else if(command['exchange'] == 'binance')
            binanceChannel.send(formattedMsg)
        else 
            exchangeChannel.send(formattedMsg)
    }
    else if(type == 'whales'){
        whaleChannel.send(formattedMsg)
    }
    else{
        generalChannel.send(formattedMsg)
    }
}