import pandas as pd
import discord
from discord.ext import commands

token = 'MTAzNDQ3NTE5MjEwMzIxNTE1NA.GJ_DMN.libfmexvfGpZB9rFxr2RSQN4p49_2evdCQVblM'

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot))
    print('Bot name: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))
    
@bot.command(name='addrole', hidden=True)
@commands.has_permissions(administrator=True)
async def add_role(ctx):
    total_role_granted = 0
    total_gleam_joined = 0
    total_abuse_user = 0
    
    gleam_result = pd.read_csv('./gleam-result-test.csv', engine='python')
    gleam_result.head()
    for idx,row in gleam_result.iterrows():
        secret_code = row[1]
        discord_id = row[2]
        total_gleam_joined+=1
        if (secret_code == 'OASYSBCG' or 'CARVANDOASYS'
            or 'OASYSBCG82' or 'OASYSBCGYGG' or 'OASYSBCGSF'
            or 'OASYSBCGRDD' or 'OASYSBCGGTP' or 'OASYSBCGNAKJU' or 'OASYSBCGGMD'):
            
                member = discord.utils.find(lambda member : member.id == discord_id, ctx.guild.members)
                role = discord.utils.find(lambda role : role.name == "test-WL", ctx.guild.roles)
                                
                if role is not None:
                    if member is not None:
                        await member.add_roles(role)
                        total_role_granted+=1
        else:               
            total_abuse_user+=1

    embed=discord.Embed(title="Command Execution Results", description="Command : !addrole", color=0x348fd5)
    embed.add_field(name="Total gleam participants", value=total_gleam_joined, inline=False)
    embed.add_field(name="Total role-granted users", value=total_role_granted, inline=False)
    embed.add_field(name="Total number of abusers", value=total_abuse_user, inline=True)
    await ctx.send(embed=embed)
                    
bot.run(token)

