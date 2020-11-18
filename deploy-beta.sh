echo "Begin deploy to Beta"
git pull origin develop
sudo docker-compose -f docker-compose-beta.yml up --build -d
echo "Finish deploy to Beta"