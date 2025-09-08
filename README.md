# Spotify Playlist Generator

A Python project that automatically generates personalized Spotify playlists based on your music preferences and listening habits. This tool leverages the Spotify Web API to curate new playlists, allowing you to discover new music and organize your favorites effortlessly.

## Features
- 🎧 **Custom Playlist Creation:** Set playlist length, mood, and genre filters.
- 🖥️ **Simple Interface:** Command-line tool for quick setup and use.

## Getting Started

### Prerequisites

- Python 3.7+
- A Spotify account
- [Spotify Developer Application](https://developer.spotify.com/dashboard/applications) (for client ID and secret)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/theo7069/SPOTIFY-PLAYLIST-GENERATOR.git
   cd SPOTIFY-PLAYLIST-GENERATOR
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Spotify API credentials:**
   - Create a `.env` file in the project root:
     ```
     SPOTIPY_CLIENT_ID=your_spotify_client_id
     SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
     SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
     ```
   - Replace the values with your credentials from the Spotify Developer Dashboard.

## Usage

Run the main script to generate a playlist:

```bash
python main.py
```

Follow the prompts to choose playlist preferences and log in to your Spotify account.

## Configuration

- Edit `config.py` to adjust default parameters like playlist name, length, or filters.
- Advanced: modify or extend the recommendation logic in `playlist_generator.py`.

## Project Structure

```
SPOTIFY-PLAYLIST-GENERATOR/
├── main.py
├── playlist_generator.py
├── config.py
├── requirements.txt
├── README.md
└── ...
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for new features, bug fixes, or suggestions.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes.
4. Push to the branch and open a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Credits

- [Spotipy](https://spotipy.readthedocs.io/) – Python client for the Spotify Web API.
- Inspired by music lovers and the open-source community.

---

Feel free to customize this README to better fit your project’s features and usage!
