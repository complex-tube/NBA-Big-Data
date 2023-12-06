import os
import subprocess
import time

from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = "Ni3oUkVW0REekscDt=ho"


class ELK:

    elastic_process: subprocess.Popen | None
    kibana_process: subprocess.Popen | None
    logstash_process: subprocess.Popen | None
    client: Elasticsearch

    def __init__(self):
        self.elastic_process = None
        self.kibana_process = None
        self.logstash_process = None

    def launch_elasticsearch(self):
        full_path_elastic = os.path.abspath('./ELK/elasticsearch/bin/elasticsearch.bat')

        try:
            self.elastic_process = subprocess.Popen(full_path_elastic, creationflags=subprocess.CREATE_NEW_CONSOLE)
        except:
            print('Не удалось запустить elasticsearch.\nДля запуска папка с elasticsearch должна находится в папке с исполнемым файлом по пути ELK/elasticsearch')
            exit(-1)

    def launch_kibana(self):
        full_path_kibana = os.path.abspath('./ELK/kibana/bin/kibana.bat')

        try:
            self.kibana_process = subprocess.Popen(full_path_kibana, creationflags=subprocess.CREATE_NEW_CONSOLE)
        except:
            print('Не удалось запустить kibana.\nДля запуска папка с kibana должна находится в папке с исполнемым файлом по пути ELK/kibana')
            exit(-1)

    def launch_logstash(self):
        full_path_logstash = os.path.abspath('./ELK/logstash/bin/logstash.bat')
        full_path_to_games_config = os.path.abspath('./ELK/logstash/config/games.conf')
        with open(full_path_to_games_config) as f:
            lines = f.readlines()
        full_path_games_data = os.path.abspath('./data/games')
        lines[2] = "                path => \"" + full_path_games_data + "\\*.csv\"\n"
        lines[2] = lines[2].replace('\\', '/')
        with open(full_path_to_games_config, 'w') as f:
            for line in lines:
                f.write(line)
        full_path_to_stats_config = os.path.abspath('./ELK/logstash/config/stats.conf')
        with open(full_path_to_stats_config) as f:
            lines = f.readlines()
        full_path_stats_data = os.path.abspath('./data/stats')
        lines[2] = "                path => \"" + full_path_stats_data + "\\*.csv\"\n"
        lines[2] = lines[2].replace('\\', '/')
        with open(full_path_to_stats_config, 'w') as f:
            for line in lines:
                f.write(line)

        self.logstash_process = subprocess.Popen(full_path_logstash, creationflags=subprocess.CREATE_NEW_CONSOLE)
        pass

    def connect_to_elastic(self):
        print('Попытка подключения к ElasticSearch')
        self.client = Elasticsearch(
            "http://localhost:9200",
            basic_auth=("elastic", ELASTIC_PASSWORD)
        )
        while self.client.ping() != True:
            time.sleep(1)
            print('Повторная попытка подключения к ElasticSearch')
            self.client = Elasticsearch(
                "http://localhost:9200",
                basic_auth=("elastic", ELASTIC_PASSWORD)
            )
        print("ElasticSearch успешно запущен")

    def delete_indices(self):
        if self.client.indices.exists(index='records-stats'):
            self.client.indices.delete(index='records-stats')
        if self.client.indices.exists(index='records-games'):
            self.client.indices.delete(index='records-games')

    def clear_null_file(self):
        full_path_null = os.path.abspath('./ELK/logstash/NULL')
        open(full_path_null, 'w').close()

