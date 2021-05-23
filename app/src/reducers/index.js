export const getWeather = async (api) => {
    const response = await fetch(api);
    if (!response.ok) {
        // throw an error if response has not successed
      throw new Error(`${response.status}, ${response.statusText}`);
    } else {
        return await response.json();
    }
}

export const updateWeather = (dispatch, data) => {
    let weather = {};
    weather.temprature = {
        unit: data.data.unit
    };
    weather.temprature.value = data.data.temp;
    weather.description = data.data.description;
    weather.iconId = `http://openweathermap.org/img/w/${data.data.icon}.png`;
    weather.city = data.data.name;
    weather.country = data.data.country;
    weather.date = data.data.date;

    dispatch({
        type: "UPDATE_WEATHER",
        payload: weather
    });
};

const reducer = (state, action) => {
    const { type, payload } = action;
    switch (type) {
        case "SET_ERROR":
            return {
                ...state,
                error: payload.error,
                city: payload.city,
                weather: null
            };
        case "SET_LOCATION":
            return {
                ...state,
                latitude: payload.latitude,
                longitude: payload.longitude
            };
        case "UPDATE_WEATHER":
            return {
                ...state,
                weather: payload,
                error: null,
                city: payload.city
            };
        default:
            return state;
    }
};

export default reducer;