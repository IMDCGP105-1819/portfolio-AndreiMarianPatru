song="""I got a song filled with shit for the strong-willed
When the world gives you a raw deal
Sets you off 'til you scream, "Piss off! Screw you!"
When it talks to you like you don't belong
Or tells you you're in the wrong field
When something's in your mitochondrial
'Cause it latched on to you, like—

Knock knock, let the devil in
Manevolent as I've ever been, head is spinnin'
This medicine's screamin', "L-L-L-Let us in!"
L-L-Like like a salad bowl, Edgar Allan Poe
Bedridden, shoulda been dead a long time ago
Liquid Tylenol, gelatins, think my skeleton's meltin'
Wicked, I get all high when I think I've smelled the scent
Of elephant manure—hell, I meant Kahlúa
Screw it, to hell with it, I went through hell with accelerants
And blew up my-my-myself again
Volkswagen, tailspin, bucket matches my pale skin
Mayo and went from Hellmann's and being rail thin
Filet-o-Fish, Scribble Jam, Rap Olympics '97 Freaknik
How can I be down? Me and Bizarre in Florida
Proof's room slept on the floor of the motel then
Dr. Dre said "hell yeah!"
And I got his stamp like a postcard, word to Mel-Man
And I know they're gonna hate
But I don't care, I barely can wait
To hit them with the snare and the bass
Square in the face, this fuckin' world better prepare to get laced
Because they're gonna taste my—

Venom, (I got that) adrenaline momentum
And I'm not knowin' when I'm
Ever gonna slow up and I’m
Ready to snap any moment I'm
Thinkin' it's time to go get 'em
They ain't gonna know what hit 'em
(W-W-When they get bit with the—)
Venom, (I got that) adrenaline momentum
And I'm not knowin' when I'm
Ever gonna slow up and I'm
Ready to snap any moment I'm
Thinkin' it's time to go get 'em
They ain't gonna know what hit 'em
(W-W-When they get bit with the—)

I said knock knock, let the devil in
Shotgun p-p-pellets in the felt pen
Cocked, fuck around and catch a hot one
It-it's evident I'm not done
V-Venomous, the thoughts spun
Like a web and you just caught in 'em
Held against your will like a hubcap or mud flap
Beat strangler attack
So this ain't gonna feel like a love tap
Eat painkiller pills, fuck up the track
Like, what's her name's at the wheel? Danica Patrick
Threw the car into reverse at the Indy, a nut crashin'
Into ya, the back of it just mangled steel
My Mustang and the Jeep Wrangler grill
With the front smashed, much as my rear fender, assassin
Slim be a combination of an actual kamikaze and Gandhi (Gandhi)
Translation, I will probably kill us both
When I end up back in India
You ain't gonna be able to tell what the fuck's happenin' to you
When you're bit with the—

Venom, adrenaline momentum
And I'm not knowin' when I'm
Ever gonna slow up and I’m
Ready to snap any moment I'm
Thinkin' it's time to go get 'em
They ain't gonna know what hit 'em
(W-W-When they get bit with the—)
Venom, (I got that) adrenaline momentum
And I'm not knowin' when I'm
Ever gonna slow up and I'm
Ready to snap any moment I'm
Thinkin' it's time to go get 'em
They ain't gonna know what hit 'em
(W-W-When they get bit with the—)

I said knock knock, let the devil in
Alien, E-E-Elliott phone home
Ain't no telling when this chokehold
On this game will end, I'm loco
Became a Symbiote, so
My fangs are in your throat, ho
You're snake-bitten with my—venom
With the ballpoint pen I'm
Gun cocked, bump stock, double-aught, buckshot
Tire thumper, a garrote, tie a couple knots
Fired up and caught fire, juggernaut
Punk rock, bitch, it's goin' down like Yung Joc
'Cause the Doc put me on like sunblock
Why the fuck not, you only get one shot
Ate shit 'til I can't taste it
Chased it with straight liquor
Then paint thinner, then drank 'til I faint
And awake with a headache
And I take anything in rectangular shape
Then I wait to face the demons I'm bonded to
'Cause they're chasin' me but I'm part of you
So escapin' me is impossible
I latch onto you like a—parasite
And I probably ruined your parents' life
And your childhood too
'Cause if I'm the music that y'all grew up on
I'm responsible for you retarded fools
I'm the super villain Dad and Mom was losin' their marbles to
You marvel that? Eddie Brock is you
And I'm the suit, so call me—

Venom, (I got that) adrenaline momentum
And I'm not knowin' when I'm
Ever gonna slow up and I’m
Ready to snap any moment I'm
Thinkin' it's time to go get 'em
They ain't gonna know what hit 'em
(W-W-When they get bit with the—)
Venom, (I got that) adrenaline momentum
And I'm not knowin' when I'm
Ever gonna slow up and I'm
Ready to snap any moment I'm
Thinkin' it's time to go get 'em
They ain't gonna know what hit 'em
(W-W-When they get bit with the—)"""
lyrics={}
mostfreq=[]
zlist=[]
listofwords=song.split(" ")
for x in listofwords:
    if x in lyrics:
        lyrics[x]+=1
    else:
        lyrics[x]=1
maxi=max(lyrics.values())
for x in lyrics:
    if lyrics[x]==maxi:
        mostfreq.append(x)
print(mostfreq)
z=int(input("Enter your number:  "))
for x in lyrics:
    if lyrics[x]>=z:
        zlist.append((x,lyrics.get(x)))
output=list(reversed(sorted(zlist, key=lambda x: x[-1])))
print(output)
