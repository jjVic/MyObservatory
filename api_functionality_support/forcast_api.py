import datetime
from support import general

from support.api_base import APIBase

class ForcastAPI(APIBase):
    def get_forcast_json(self):
        response_data = self.get_response_data(general.request_method["GET"], general.forcast_data["api-path"])
        return self.load_data_in_json(response_data)

    def get_forcast_response_status(self):
        return self.get_response_status_code(general.request_method['GET'], general.forcast_data["api-path"])

    def get_relative_humidity_the_day_after_tomorrow(self):
        today = datetime.datetime.now()
        today_formatted = today.strftime("%Y%m%d")
        print(f'Today is:{today_formatted}')

        # get the day after tomorrow
        delta = datetime.timedelta(days=2)
        the_day_after_tomorrow =today + delta
        the_day_after_tomorrow_formatted = the_day_after_tomorrow.strftime("%Y%m%d")
        print(f'The day after tomorrow is: {the_day_after_tomorrow_formatted}')

        max_humidity = ""
        min_humidity = ""
        forcast_data = self.get_forcast_json()
        for item in forcast_data["forecast_detail"]:
            if item["forecast_date"] == the_day_after_tomorrow_formatted:
                max_humidity = item["max_rh"]
                min_humidity = item["min_rh"]

        return f'The relative humidity on the day after tomorrow {the_day_after_tomorrow_formatted} is {str(min_humidity)}-{str(max_humidity)}%'


