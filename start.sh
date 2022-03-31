if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Emilyoftg/Extra-1.0.git /Extra-1.0
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Extra-1.0
fi
cd /Extra-1.0
pip3 install -U -r requirements.txt
echo "Starting Nathalia....🔥"
python3 bot.py
