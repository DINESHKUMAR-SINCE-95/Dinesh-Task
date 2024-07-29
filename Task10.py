
Try the new cross-platform PowerShell https://aka.ms/pscore6

(.venv) PS C:\Users\Dell\PycharmProjects\requirement.txt> pip freeze > requirements.txt
(.venv) PS C:\Users\Dell\PycharmProjects\requirement.txt> 
(.venv) PS C:\Users\Dell\PycharmProjects\requirement.txt> pip freeze > requirements.txt
(.venv) PS C:\Users\Dell\PycharmProjects\requirement.txt> 
(.venv) PS C:\Users\Dell\PycharmProjects\requirement.txt> pip install Flask<2.0
Collecting Flask<2.0
  Obtaining dependency information for Flask<2.0 from https://files.pythonhosted.org/packages/e8/6d/994208daa354f68fd89a34a8bafbeaab26fda84e7af1e35bdaed02b667e6/
Flask-1.1.4-py2.py3-none-any.whl.metadata
  Downloading Flask-1.1.4-py2.py3-none-any.whl.metadata (4.6 kB)
Collecting Werkzeug<2.0,>=0.15 (from Flask<2.0)
  Obtaining dependency information for Werkzeug<2.0,>=0.15 from https://files.pythonhosted.org/packages/cc/94/5f7079a0e00bd6863ef8f1da638721e9da21e5bacee597595b3
18f71d62e/Werkzeug-1.0.1-py2.py3-none-any.whl.metadata
  Downloading Werkzeug-1.0.1-py2.py3-none-any.whl.metadata (4.7 kB)
Collecting Jinja2<3.0,>=2.10.1 (from Flask<2.0)
  Obtaining dependency information for Jinja2<3.0,>=2.10.1 from https://files.pythonhosted.org/packages/7e/c2/1eece8c95ddbc9b1aeb64f5783a9e07a286de42191b7204d67b
7496ddf35/Jinja2-2.11.3-py2.py3-none-any.whl.metadata
  Downloading Jinja2-2.11.3-py2.py3-none-any.whl.metadata (3.5 kB)
Collecting itsdangerous<2.0,>=0.24 (from Flask<2.0)
  Obtaining dependency information for itsdangerous<2.0,>=0.24 from https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c
953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl.metadata
  Downloading itsdangerous-1.1.0-py2.py3-none-any.whl.metadata (3.1 kB)
Collecting click<8.0,>=5.1 (from Flask<2.0)
  Obtaining dependency information for click<8.0,>=5.1 from https://files.pythonhosted.org/packages/d2/3d/fa76db83bf75c4f8d338c2fd15c8d33fdd7ad23a9b5e57eb6c5de26
b430e/click-7.1.2-py2.py3-none-any.whl.metadata
  Downloading click-7.1.2-py2.py3-none-any.whl.metadata (2.9 kB)
Collecting MarkupSafe>=0.23 (from Jinja2<3.0,>=2.10.1->Flask<2.0)
  Obtaining dependency information for MarkupSafe>=0.23 from https://files.pythonhosted.org/packages/3f/14/c3554d512d5f9100a95e737502f4a2323a1959f6d0d01e0d0997b3
5f7b10/MarkupSafe-2.1.5-cp312-cp312-win_amd64.whl.metadata
  Downloading MarkupSafe-2.1.5-cp312-cp312-win_amd64.whl.metadata (3.1 kB)
Downloading Flask-1.1.4-py2.py3-none-any.whl (94 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 94.6/94.6 kB 897.4 kB/s eta 0:00:00

Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 82.8/82.8 kB 1.6 MB/s eta 0:00:00

Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Downloading Jinja2-2.11.3-py2.py3-none-any.whl (125 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 125.7/125.7 kB 1.2 MB/s eta 0:00:00

Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)

Downloading MarkupSafe-2.1.5-cp312-cp312-win_amd64.whl (17 kB)
Installing collected packages: Werkzeug, MarkupSafe, itsdangerous, click, Jinja2, Flask
Successfully installed Flask-1.1.4 Jinja2-2.11.3 MarkupSafe-2.1.5 Werkzeug-1.0.1 click-7.1.2 itsdangerous-1.1.0

[notice] A new release of pip is available: 23.2.1 -> 24.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip
(.venv) PS C:\Users\Dell\PycharmProjects\requirement.txt>
(.venv) PS C:\Users\Dell\PycharmProjects\requirement.txt>





### Music Player Web App using TypeScript, OOP, HTML, and Bootstrap

#### Overview

#This project involves creating a music player web application that allows users to create playlists, add audio files, search for audio and playlists, and rate both. The app will be built using TypeScript with an emphasis on Object-Oriented Programming (OOP), HTML, and Bootstrap for the UI.

#### Key Features

# 1. Audio Management:
  # - Users can add audio using URLs.
  # - Users can create multiple playlists based on genres.
  # - Users can add multiple audio files to each playlist.
   #- Users can search for audio and playlists by name.

#2.Rating System:
  # - Users can rate playlists and audio files.
   #- Average rating displayed based on ratings from 3 users, with ratings randomly generated between 1 and 5.

#3. Customization and Responsiveness:
  # - UI built with Bootstrap for responsiveness.
  # - Customizable audio player.

#### Project Structure

#1. TypeScript Classes:
 #  - `Audio`
  # - `Playlist`
  # - `User`
  # - `MusicPlayer`

#2. HTML Elements:
  # - Generated using TypeScript.

#3. Styling:
  # - Bootstrap for responsiveness.
  # - Custom styles if needed.

#### Implementation Steps

#1. setup the Project:
  # - Initialize the project with TypeScript and Bootstrap.
  #- Set up a basic HTML structure.

#2. Define TypeScript Classes:

   typescript
   class Audio {
       id: number;
       name: string;
       url: string;
       ratings: number[];

       constructor(id: number, name: string, url: string) {
           this.id = id;
           this.name = name;
           this.url = url;
           this.ratings = [];
       }

       addRating(rating: number) {
           this.ratings.push(rating);
       }

       getAverageRating() {
           if (this.ratings.length === 0) return 0;
           let sum = this.ratings.reduce((a, b) => a + b, 0);
           return sum / this.ratings.length;
       }
   }

   class Playlist {
       id: number;
       name: string;
       genre: string;
       audios: Audio[];
       ratings: number[];

       constructor(id: number, name: string, genre: string) {
           this.id = id;
           this.name = name;
           this.genre = genre;
           this.audios = [];
           this.ratings = [];
       }

       addAudio(audio: Audio) {
           this.audios.push(audio);
       }

       addRating(rating: number) {
           this.ratings.push(rating);
       }

       getAverageRating() {
           if (this.ratings.length === 0) return 0;
           let sum = this.ratings.reduce((a, b) => a + b, 0);
           return sum / this.ratings.length;
       }
   }

   class User {
       id: number;
       name: string;

       constructor(id: number, name: string) {
           this.id = id;
           this.name = name;
       }

       rateAudio(audio: Audio, rating: number) {
           audio.addRating(rating);
       }

       ratePlaylist(playlist: Playlist, rating: number) {
           playlist.addRating(rating);
       }
   }

   class MusicPlayer {
       playlists: Playlist[];
       users: User[];

       constructor() {
           this.playlists = [];
           this.users = [];
       }

       addPlaylist(playlist: Playlist) {
           this.playlists.push(playlist);
       }

       addUser(user: User) {
           this.users.push(user);
       }

       findPlaylistByName(name: string) {
           return this.playlists.filter(playlist => playlist.name.toLowerCase().includes(name.toLowerCase()));
       }

       findAudioByName(name: string) {
           let audios: Audio[] = [];
           this.playlists.forEach(playlist => {
               audios = audios.concat(playlist.audios.filter(audio => audio.name.toLowerCase().includes(name.toLowerCase())));
           });
           return audios;
       }
   }
  

# 3. Generate HTML Elements with TypeScript:

   typescript
   function createAudioElement(audio: Audio) {
       let audioElement = document.createElement('div');
       audioElement.className = 'audio';

       let audioTitle = document.createElement('h5');
       audioTitle.innerText = audio.name;
       audioElement.appendChild(audioTitle);

       let audioPlayer = document.createElement('audio');
       audioPlayer.controls = true;
       audioPlayer.src = audio.url;
       audioElement.appendChild(audioPlayer);

       let rating = document.createElement('p');
       rating.innerText = `Average Rating: ${audio.getAverageRating().toFixed(2)}`;
       audioElement.appendChild(rating);

       return audioElement;
   }

   function createPlaylistElement(playlist: Playlist) {
       let playlistElement = document.createElement('div');
       playlistElement.className = 'playlist';

       let playlistTitle = document.createElement('h5');
       playlistTitle.innerText = playlist.name;
       playlistElement.appendChild(playlistTitle);

       playlist.audios.forEach(audio => {
           let audioElement = createAudioElement(audio);
           playlistElement.appendChild(audioElement);
       });

       let rating = document.createElement('p');
       rating.innerText = `Average Rating: ${playlist.getAverageRating().toFixed(2)}`;
       playlistElement.appendChild(rating);

       return playlistElement;
   }
  

# 4. User Interface with Bootstrap:

   html
   <div class="container">
       <div id="music-player" class="row"></div>
   </div>


 typescript
   let musicPlayer = new MusicPlayer();

   // Sample data for demonstration
   let user1 = new User(1, 'User 1');
   let user2 = new User(2, 'User 2');
   let user3 = new User(3, 'User 3');

   musicPlayer.addUser(user1);
   musicPlayer.addUser(user2);
   musicPlayer.addUser(user3);

   let audio1 = new Audio(1, 'Song 1', 'url1.mp3');
   let audio2 = new Audio(2, 'Song 2', 'url2.mp3');

   let playlist1 = new Playlist(1, 'Playlist 1', 'Rock');
   playlist1.addAudio(audio1);
   playlist1.addAudio(audio2);

   musicPlayer.addPlaylist(playlist1);

   document.getElementById('music-player').appendChild(createPlaylistElement(playlist1));

   // Random rating for demonstration
   function randomRating() {
       return Math.floor(Math.random() * 5) + 1;
   }

   user1.rateAudio(audio1, randomRating());
   user2.rateAudio(audio1, randomRating());
   user3.rateAudio(audio1, randomRating());

   user1.ratePlaylist(playlist1, randomRating());
   user2.ratePlaylist(playlist1, randomRating());
   user3.ratePlaylist(playlist1, randomRating());

   document.getElementById('music-player').innerHTML = '';
   document.getElementById('music-player').appendChild(createPlaylistElement(playlist1));

   
 


# 5. Hosting and Submission:
   - Push your code to GitHub.
   - Host your webpage on Netlify.

Summary

This project demonstrates the use of TypeScript and OOP concepts to create a functional music player web app with features like audio and playlist management, search, and rating system. The UI is built with Bootstrap to ensure responsiveness, and all HTML elements are generated using TypeScript.








