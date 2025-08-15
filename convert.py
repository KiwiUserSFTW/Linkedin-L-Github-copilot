import os
import yaml  # PyYAML package is required

# Try to import Mutagen for reading MP3 metadata
try:
    from mutagen.mp3 import MP3
    MUTAGEN_AVAILABLE = True
except ImportError:
    MUTAGEN_AVAILABLE = False

def list_mp3_files(audio_dir):
    if not os.path.isdir(audio_dir):
        print(f"Audio directory '{audio_dir}' not found.")
        return []
    return [f for f in os.listdir(audio_dir) if f.lower().endswith('.mp3')]

def get_duration(file_path):
    if MUTAGEN_AVAILABLE:
        try:
            audio = MP3(file_path)
            duration_in_seconds = audio.info.length
            minutes = int(duration_in_seconds // 60)
            seconds = int(duration_in_seconds % 60)
            return f"{minutes:02d}:{seconds:02d}"
        except Exception as e:
            print(f"Error reading duration for {file_path}: {e}")
    return "00:00"

if __name__ == '__main__':
    # The audio directory is assumed to be in the same workspace directory.
    current_dir = os.getcwd()
    audio_dir = os.path.join(current_dir, 'audio')
    
    mp3_files = list_mp3_files(audio_dir)
    
    if mp3_files:
        result = {'mp3_files': []}
        for file in mp3_files:
            full_path = os.path.join(audio_dir, file)
            file_entry = {
                'filename': file,
                'title': file,         # default title as filename
                'comments': "",        # no comments available
                'duration': get_duration(full_path)
            }
            result['mp3_files'].append(file_entry)
    else:
        result = {'message': "No MP3 files found."}
    
    # Print YAML formatted output
    print(yaml.dump(result, default_flow_style=False))