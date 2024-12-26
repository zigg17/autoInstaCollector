DIRECTORY="/Users/jakeziegler/Desktop/PROJECTS/INSTA/data/like-comment/Screenshots1"

find "$DIRECTORY" -type f | while read -r FILE; do
    sudo chown jakeziegler:staff "$FILE"
    sudo chmod u+w "$FILE"
    echo "Updated: $FILE"
done