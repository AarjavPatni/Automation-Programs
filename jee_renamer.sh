#!/usr/bin/env bash

notify-send 'JEE Renamer Started'
(
    flock -n 200 || exit 1
    while inotifywait -r "/home/aarjav/pCloudDrive" -e move -e create -e delete; do
        sleep 2
        # List the path to all directories named "Class PDFs" in ~/pCloudDrive and subdirectories
        PDFPaths=()
        readarray -t PDFPaths < <(find ~/pCloudDrive | grep -e '/Class PDFs$')

        # List all the directories in each path in PDFPaths
        Paths=()
        readarray -t Paths < <(for Path in "${PDFPaths[@]}"; do find "$Path" -type d; done)

        for folder in "${Paths[@]}"; do
            pdfs=()
            readarray -t pdfs < <(find "$folder" -maxdepth 1 -type f -name '*.pdf' -printf '%Ts\t%p\n' | sort -n | cut -f2)
            n=1
            for pdf in "${pdfs[@]}"; do
                # Replace underscores with spaces. Remove "_with_anno" from filenames.
                # If filename contains underscores, rename the file.
                if [[ "$pdf" =~ "_" ]]; then
                    echo "Renaming $pdf"
                    mv -i "$pdf" "$(echo "$pdf" | sed 's/_with_anno//g' | sed 's/_/ /g' | sed 's/__/ /g' | sed 's/  */ /g' | sed 's/Doubt Clearing Session/DCS/g')"
                    # Change the variable to the new filename
                    pdf="$(echo "$pdf" | sed 's/_with_anno//g' | sed 's/_/ /g' | sed 's/__/ /g' | sed 's/  */ /g' | sed 's/Doubt Clearing Session/DCS/g')"
                fi
                base=$(basename "$pdf")
                dir=$(dirname "$pdf")
                if [[ "${base:0:1}" != 'L' ]] && [[ ${base:1:2} =~ ^[^0-9] ]]; then
                    notify-send "JEE Renamer" "Renaming $base to L$n $base"
                    mv "$pdf" "${dir}//L${n} ${base}"
                fi
                ((n++))
            done
        done
    done
) 200>/var/lock/jee_renamer.lock
