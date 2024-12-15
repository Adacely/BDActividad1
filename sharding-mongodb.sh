# configurar replica set

docker network create mongoCluster

docker run -d --rm -p 27017:27017 --name mongo1 --network mongoCluster mongo:5 mongod --configsvr --replSet myReplicaSet --bind_ip localhost,mongo1

docker run -d --rm -p 27018:27017 --name mongo2 --network mongoCluster mongo:5 mongod --configsvr --replSet myReplicaSet --bind_ip localhost,mongo2
 
docker run -d --rm -p 27019:27017 --name mongo3 --network mongoCluster mongo:5 mongod --configsvr --replSet myReplicaSet --bind_ip localhost,mongo3


docker exec -it mongo1 mongosh --eval "rs.initiate({
 _id: \"myReplicaSet\",
 configsvr: true,
 members: [
   {_id: 0, host: \"mongo1:27017\"},
   {_id: 1, host: \"mongo2:27017\"},
   {_id: 2, host: \"mongo3:27017\"}
 ]
})"

docker run -d --rm -p 27017:27017 --name mongo1 --network mongoCluster mongo:5 mongod --port 27017 --configsvr --replSet myReplicaSet 
docker run -d --rm -p 27018:27017 --name mongo2 --network mongoCluster mongo:5 mongod --port 27017 --configsvr --replSet myReplicaSet 
 
docker run -d --rm -p 27019:27017 --name mongo3 --network mongoCluster mongo:5 mongod --port 27017 --configsvr --replSet myReplicaSet 

# crear shard

docker run -d --name shard-X-node-a --network mongoCluster -p 27110:27017 mongo:5 mongod --port 27017 --shardsvr --replSet myReplicaShardSet
docker run -d --name shard-X-node-b --network mongoCluster -p 27120:27017 mongo:5 mongod --port 27017 --shardsvr --replSet myReplicaShardSet
docker run -d --name shard-X-node-c --network mongoCluster -p 27130:27017 mongo:5 mongod --port 27017 --shardsvr --replSet myReplicaShardSet

docker exec -it shard-X-node-a mongosh --eval "rs.initiate({
 _id: \"myReplicaShardSet\",
 members: [
   {_id: 0, host: \"shard-X-node-a:27017\"},
   {_id: 1, host: \"shard-X-node-b:27017\"},
   {_id: 2, host: \"shard-X-node-c:27017\"}
 ]
})"


# Crear routers

docker run -d  --name router-1 --network mongoCluster -p 27141:27017 mongo:5 mongos --port 27017 --configdb myReplicaSet/mongo1:27017,mongo2:27017,mongo3:27017 --bind_ip_all

docker run -d --name router-2 --network mongoCluster -p 27142:27017 mongo:5 mongos --port 27017 --configdb myReplicaSet/mongo1:27017,mongo2:27017,mongo3:27017 --bind_ip_all


# agregar shard al cluster


sh.addShard( "myReplicaShardSet/shard-X-node-a:27017,shard-X-node-b:27017,shard-X-node-c:27017")

# Verificar shard activos

sh.status()

# Habilitar BD para sharding

sh.enableSharding("TorneoDeportivo")

# Importar registros




mongod --configsvr --replSet <replica set name> --dbpath <path> --bind_ip localhost,<hostname(s)|ip address(es)>