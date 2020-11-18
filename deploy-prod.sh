echo "Begin deploy to Prod"
git pull origin master
sudo docker-compose -f docker-compose-prod.yml up --build -d
echo "Finish deploy to Prod"