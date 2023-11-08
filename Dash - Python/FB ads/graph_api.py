import requests
import json
import pandas as pd



class GraphAPI:
    def __init__(self, fb_api):
        self.base_url = "https://graph.facebook.com/v18.0/"
        self.api_fields = ["campaign_name", "campaign_id", "spend"]
        self.token = "&access_token=" + fb_api
        


    def get_insights(self, ad_acc, level="campaign"):
        url = self.base_url + "act_" + str(ad_acc)
        url += "/insights?level=" +  level
        url += "&fields=" + ",".join(self.api_fields)

        data = requests.get(url + self.token)
        data = json.loads(data._content.decode("utf-8"))

    def get_campaign_status(self, ad_acc):
        url = self.base_url + "act_" + str(ad_acc)
        url += "/campaigns?fields=name,status,adsets{name, id}"
        data = requests.get(url + self.token)
        return json.loads(data._content.decode("utf-8"))

    def get_adset_status(self, ad_acc):
        url = self.base_url + "act_" + str(ad_acc)
        url += "/adsets?fields=name,status,id"
        data = requests.get(url + self.token)
        return json.loads(data._content.decode("utf-8"))

    def get_data_over_time(self, campaign):
        url = self.base_url + str(campaign)
        url += "/insights?fields="+ ",".join(self.api_fields)
        url += "&date_preset=last_30d&time_increment=1"

        data = requests.get(url + self.token)
        data = json.loads(data._content.decode("utf-8"))
        return data



if __name__ == "__main__":
    fb_api = open("tokens/fb_token").read()
    ad_acc = "1426845550909398"

    self = GraphAPI(fb_api)


    self.get_insights(1426845550909398)
    self.get_campaign_status(ad_acc)


