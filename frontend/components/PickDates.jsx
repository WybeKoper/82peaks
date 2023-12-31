import React, { useState } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

const PickDates = () => {
  const [dateRange, setDateRange] = useState([null, null]);
  const [startDate, endDate] = dateRange;
  const today = new Date();
  const tomorrow = new Date();
  const latestDate = new Date();
  tomorrow.setDate(today.getDate() + 1);
  latestDate.setDate(today.getDate() + 5);

  const [mountain, setMountain] = useState([]);

  const fetchMountain = async () => {
    if (!(startDate == null || endDate == null)) {
      const response = await fetch(
        "https://h9goc3x5r6.execute-api.eu-central-1.amazonaws.com/example-stage/bestpeaks" +
          "?" +
          "startDate=" +
          startDate.getFullYear() +
          "-" +
          (startDate.getMonth() + 1) +
          "-" +
          startDate.getDate() +
          "&" +
          "endDate=" +
          endDate.getFullYear() +
          "-" +
          (endDate.getMonth() + 1) +
          "-" +
          endDate.getDate()
      );
      const data = await response.json();
      setMountain(data);
    }
  };

  return (
    <div className="">
      <div className="flex items-center justify-center">
        <div>
          <DatePicker
            className="p-1 bg-slate-200 border rounded border-gray-800"
            selectsRange={true}
            minDate={tomorrow}
            maxDate={latestDate}
            startDate={startDate}
            endDate={endDate}
            onChange={(update) => {
              setDateRange(update);
            }}
            placeholderText="When do you want to climb?"
            isClearable={true}
          />
        </div>
        <div className="pl-5">
          <button
            className="bg-slate-200  p-1 border rounded border-gray-800 hover:bg-slate-500"
            onClick={fetchMountain}
          >
            Find Peak
          </button>
        </div>
      </div>
      <div className="pt-5 justify-center">
        {mountain.map((mont) => {
          return (
            <div
              key={mont.mountain_name}
              className="flex w-full items-center justify-center"
            >
              <div className="flex">
                <div className="flex items-end">
                  <div className="p-1 text-sm">Wind km/h</div>
                </div>
                <div className="bg-slate-300 border-solid border-2 rounded border-gray-800">
                  <div className="flex items-center justify-center p-5">
                    <div className="p-1 text-5xl">{mont.mountain_name}</div>
                    <div className="p-1 pl-10 underline text-sky-600">
                      <a href={mont.url} target="_blank">
                        Detailed Forecast
                      </a>
                    </div>
                  </div>
                  <div className="flex items-center justify-center divide-x-2 divide-gray-400">
                    {mont.weather.map((single_day) => (
                      <div key={single_day.id} className="">
                        <div className="bg-slate-200">
                          <div>{single_day.day_of_week} </div>
                          <div>{single_day.date} </div>
                        </div>
                        <div className="flex bg-slate-200">
                          {single_day.detailed_weather.map((time_period) => (
                            <div className="" key={time_period.id}>
                              <div className="bg-slate-200">
                                {time_period.time}
                              </div>
                              <img
                                className="box-border h-20 w-20"
                                src={time_period.weather_icon}
                              />
                              <div className="box-border h-16 w-20">
                                {time_period.weather_description}
                              </div>
                              <div className="">{time_period.wind}</div>
                            </div>
                          ))}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default PickDates;
