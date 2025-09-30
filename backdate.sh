#!/bin/bash

# 1. Configuration
start_date="2025-08-01"
end_date="2025-09-30"
days_to_commit=10
commits_per_day=3

# 2. Get all files and folders (excluding hidden/scripts)
all_files=$(find . -maxdepth 2 -type f -not -path '*/.*' -not -name "*.sh")
all_folders=(*/)

# 3. Pick 10 random unique days between Aug and Sept
target_days=()
for ((i=0; i<days_to_commit; i++)); do
    # Random day offset from Aug 1st (61 days total in Aug/Sep)
    random_offset=$((RANDOM % 61))
    target_days+=("$random_offset")
done

# 4. Start Committing
for day_offset in "${target_days[@]}"; do
    for ((c=0; c<commits_per_day; c++)); do
        # Generate random time (09:00 - 21:00)
        random_hour=$(printf "%02d" $((9 + RANDOM % 12)))
        random_min=$(printf "%02d" $((RANDOM % 60)))
        
        # Calculate precise date
        commit_date=$(date -d "$start_date + $day_offset days $random_hour:$random_min:00" +"%Y-%m-%dT%H:%M:%S")
        
        # Pick one random file to stage
        random_file=$(echo "$all_files" | shuf -n 1)
        
        if [ -n "$random_file" ]; then
            export GIT_AUTHOR_DATE="$commit_date"
            export GIT_COMMITTER_DATE="$commit_date"
            
            git add "$random_file"
            git commit -m "Update: working on $(basename "$random_file")"
            
            echo "Committed $random_file on $commit_date"
        fi
    done
done

# 5. Final commit for anything left over
export GIT_AUTHOR_DATE="2025-09-30T17:00:00"
export GIT_COMMITTER_DATE="2025-09-30T17:00:00"
git add .
git commit -m "Final project synchronization"
unset GIT_AUTHOR_DATE GIT_COMMITTER_DATE
