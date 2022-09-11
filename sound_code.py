# Code for loading the sound used while recognizing the currency:

# Make sure to run this cell only once (once you have the audio files, you no longer need to run this cell)
from gtts import gTTS
from playsound import playsound
import inflect

# 50 piasters sound
text05 = "مَعَكْ نِصْفُ جُنَيْهْ"
g = gTTS(text=text05 , lang= 'ar')
g.save('audio05.mp3')

# 1 pound sound
text1 = "مَعَكْ جُنَيْهْ"
g = gTTS(text=text1 , lang= 'ar')
g.save('audio1.mp3')

# 5 pounds sound
text5 = "مَعَكْ خَمْسَةُ جُنَيْهَاتٍ"
g = gTTS(text=text5 , lang= 'ar')
g.save('audio5.mp3')

# 10 pounds sound
text10 = "مَعَكْ عَشْرَةُ جُنَيْهاتٍ"
g = gTTS(text=text10 , lang= 'ar')
g.save('audio10.mp3')

# 20 pounds sound
text20 = "مَعَكْ عُشْرُونَ جُنَيْهاً"
g = gTTS(text=text20 , lang= 'ar')
g.save('audio20.mp3')

# 50 pounds sound
text50 = "مَعَكْ خَمْسُونَ جُنَيْهاً"
g = gTTS(text=text50 , lang= 'ar')
g.save('audio50.mp3')

# 100 pounds sound
text100 = "مَعَكْ مِائَةُ جُنَيْهْ"
g = gTTS(text=text100 , lang= 'ar')
g.save('audio100.mp3')

# 200 pounds sound
text200 = "مَعَكْ مِائَتَيْنِ جُنَيْهْ"
g = gTTS(text=text200 , lang= 'ar')
g.save('audio200.mp3')