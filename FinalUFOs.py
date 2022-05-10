'''
Name: McKinley Smith
Class: CS230-1
Description: coding to make a cloud streamlit webiste to show case the data of UFO sighting around the world.
The data points will be presented in a map form, then shape, location, and frequency of sighting will be shown through
drop down menus depending on country/shape selected.
'''
import streamlit as st
import pydeck as pdk
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_rows", None, "display.max_columns", None, 'display.width', None, 'max_colwidth', None)

dfUFO = pd.read_csv("UFOdata.csv")  # reading in CSV file to work with
dfUFO1 = dfUFO.drop(["duration (seconds)","duration (hours/min)"], axis = 1).astype(str)# fixing problems so the data frame can be shown

# Creating a side bar to toggle between shape graphs, location graphs, and maps
st.sidebar.title("Different ways to view data")
options = [" ","Maps", "Shapes", "Locations"]
selectoptions = st.sidebar.selectbox("How would you like to view the data?",options)

#splitting to only show what is in each option of selectbox
if selectoptions == " ":
    st.title("UFO Sightings by Location and Shape Around the World")  # titling page
    st.write("Data frame Used for the graphs and map")
    st.write(dfUFO1)  #puting dataframe online
elif selectoptions == "Maps":  # is the new page and shows a simple map of all the UFO sightings
    st.write("The Map of UFO Sightings")
    options = ["", "us","ca","de","gb","au"]
    selectmaps = st.sidebar.selectbox("Scatter Plot Maps of Sightings Based on Country",options)
    if selectmaps=="":  # the everywhere map
        dfUFO1['Lat']=pd.to_numeric(dfUFO1['Lat'])  # forces the columns to be numeric so the long and lat data can be accessed correctly
        dfUFO1['Lon']=pd.to_numeric(dfUFO1['Lon'])
        dfUFO1.rename(columns={"Lat":"lat", "Lon": "lon"}, inplace=True)  # reassigns names to Lat and Lon columns so pandas will accept it
        st.title('Simple Map')
        st.map(dfUFO1)
    elif selectmaps=="us":  # From here on coding is the same, but focuses on individual countires and scatter plots for them
        st.title("US Scatterplot Map")
        usmap = dfUFO1[dfUFO1["country"] == "us"]
        usmap['Lat']=pd.to_numeric(usmap['Lat'])
        usmap['Lon']=pd.to_numeric(usmap['Lon'])
        usmap.rename(columns={"Lat":"lat", "Lon": "lon"}, inplace= True)
        view_state = pdk.ViewState(latitude=usmap["lat"].mean(),longitude=usmap["lon"].mean(),zoom=30,pitch=0) #view area, centering
        layer1 = pdk.Layer(type = 'ScatterplotLayer',data=usmap,get_position='[lon, lat]',get_radius=2500,get_color=[0,0,255],pickable=True)  # big dot can be seen from very zoomed out
        layer2 = pdk.Layer('ScatterplotLayer',data=usmap,get_position='[lon, lat]',get_radius=100,get_color=[255,0,255],pickable=True)  #small dot more focused when zoomed in
        tool_tip = {"datetime": "Date spotted: <br/> <b>{datetime}</b>","style": { "backgroundColor": "orange","color": "white"}}
        map = pdk.Deck(map_style='mapbox://styles/mapbox/outdoors-v11',initial_view_state=view_state, layers=[layer1,layer2], tooltip= tool_tip)  # how to plot map
        st.pydeck_chart(map)
    elif selectmaps=="ca":
        st.title("CA Scatterplot Map")
        camap = dfUFO1[dfUFO1["country"] == "ca"]
        camap['Lat']=pd.to_numeric(camap['Lat'])
        camap['Lon']=pd.to_numeric(camap['Lon'])
        camap.rename(columns={"Lat":"lat", "Lon": "lon"}, inplace= True)
        view_state = pdk.ViewState(latitude=camap["lat"].mean(),longitude=camap["lon"].mean(),zoom=30,pitch=0)
        layer1 = pdk.Layer(type = 'ScatterplotLayer',data=camap,get_position='[lon, lat]',get_radius=2500,get_color=[0,0,255],pickable=True)
        layer2 = pdk.Layer('ScatterplotLayer',data=camap,get_position='[lon, lat]',get_radius=100,get_color=[255,0,255],pickable=True)
        tool_tip = {"datetime": "Date spotted: <br/> <b>{datetime}</b>","style": { "backgroundColor": "orange","color": "white"}}
        map = pdk.Deck(map_style='mapbox://styles/mapbox/outdoors-v11',initial_view_state=view_state, layers=[layer1,layer2], tooltip= tool_tip)
        st.pydeck_chart(map)
    elif selectmaps=="de":
        st.title("DE Scatterplot Map")
        demap = dfUFO1[dfUFO1["country"] == "de"]
        demap['Lat']=pd.to_numeric(demap['Lat'])
        demap['Lon']=pd.to_numeric(demap['Lon'])
        demap.rename(columns={"Lat":"lat", "Lon": "lon"}, inplace= True)
        view_state = pdk.ViewState(latitude=demap["lat"].mean(),longitude=demap["lon"].mean(),zoom=30,pitch=0)
        layer1 = pdk.Layer(type = 'ScatterplotLayer',data=demap,get_position='[lon, lat]',get_radius=2500,get_color=[0,0,255],pickable=True)
        layer2 = pdk.Layer('ScatterplotLayer',data=demap,get_position='[lon, lat]',get_radius=100,get_color=[255,0,255],pickable=True)
        tool_tip = {"datetime": "Date spotted: <br/> <b>{datetime}</b>","style": { "backgroundColor": "orange","color": "white"}}
        map = pdk.Deck(map_style='mapbox://styles/mapbox/outdoors-v11',initial_view_state=view_state, layers=[layer1,layer2], tooltip= tool_tip)
        st.pydeck_chart(map)
    elif selectmaps=="gb":
        st.title("GB Scatterplot Map")
        gbmap = dfUFO1[dfUFO1["country"] == "gb"]
        gbmap['Lat']=pd.to_numeric(gbmap['Lat'])
        gbmap['Lon']=pd.to_numeric(gbmap['Lon'])
        gbmap.rename(columns={"Lat":"lat", "Lon": "lon"}, inplace= True)
        view_state = pdk.ViewState(latitude=gbmap["lat"].mean(),longitude=gbmap["lon"].mean(),zoom=30,pitch=0)
        layer1 = pdk.Layer(type = 'ScatterplotLayer',data=gbmap,get_position='[lon, lat]',get_radius=2500,get_color=[0,0,255],pickable=True)
        layer2 = pdk.Layer('ScatterplotLayer',data=gbmap,get_position='[lon, lat]',get_radius=100,get_color=[255,0,255],pickable=True)
        tool_tip = {"datetime": "Date spotted: <br/> <b>{datetime}</b>","style": { "backgroundColor": "orange","color": "white"}}
        map = pdk.Deck(map_style='mapbox://styles/mapbox/outdoors-v11',initial_view_state=view_state, layers=[layer1,layer2], tooltip= tool_tip)
        st.pydeck_chart(map)
    elif selectmaps=="au":
        st.title("AU Scatterplot Map")
        aumap = dfUFO1[dfUFO1["country"] == "au"]
        aumap['Lat']=pd.to_numeric(aumap['Lat'])
        aumap['Lon']=pd.to_numeric(aumap['Lon'])
        aumap.rename(columns={"Lat":"lat", "Lon": "lon"}, inplace= True)
        view_state = pdk.ViewState(latitude=aumap["lat"].mean(),longitude=aumap["lon"].mean(),zoom=30,pitch=0)
        layer1 = pdk.Layer(type = 'ScatterplotLayer',data=aumap,get_position='[lon, lat]',get_radius=2500,get_color=[0,0,255],pickable=True)
        layer2 = pdk.Layer('ScatterplotLayer',data=aumap,get_position='[lon, lat]',get_radius=100,get_color=[255,0,255],pickable=True)
        tool_tip = {"datetime": "Date spotted: <br/> <b>{datetime}</b>","style": { "backgroundColor": "orange","color": "white"}}
        map = pdk.Deck(map_style='mapbox://styles/mapbox/outdoors-v11',initial_view_state=view_state, layers=[layer1,layer2], tooltip= tool_tip)
        st.pydeck_chart(map)
elif selectoptions == "Shapes":
    st.write("The Shapes UFO's Take and their Frequency")
    sdfShapes = dfUFO.loc[:,["shape","country","duration (seconds)"]]
    shapes = {}
    for i in sdfShapes["shape"]:  # used to count how many times a shape occurs
        if i not in shapes:
            shapes[i]= 1
        if i in shapes:
            shapes[i]+=1
    shapes.pop("nan")  # removes entries where shape wasn't listed
    shapekeys = list(shapes.keys())  # makes individual lists of keys and values
    shapevalues = list(shapes.values())
    selectshape = st.sidebar.selectbox("Would you like to see the duration of a shape?",["",'cylinder', 'light', 'circle', 'sphere', 'disk', 'fireball', 'unknown', 'oval', 'other', 'cigar', 'rectangle', 'chevron', 'triangle', 'formation', 'delta', 'changing', 'egg', 'diamond', 'flash', 'teardrop', 'cone', 'cross', 'pyramid', 'round', 'crescent', 'flare', 'hexagon', 'dome', 'changed'])
    if selectshape == "":  # create pie chart of all shapes
        fig, ax = plt.subplots()
        ax.pie(shapevalues, labels = shapekeys,
           textprops={'size': 'xx-small'}, rotatelabels=30, labeldistance= .7, counterclock=False)  # to make the chart more legible
        st.pyplot(fig)
    elif selectshape=="cylinder":
        cylinders = sdfShapes[sdfShapes["shape"] == "cylinder"]  # selects all the data from the smaller df that are cylinder shaped, same every other one
        shape1 = {}
        for i in cylinders["country"]:  # create the count for how many times shape seen in each country
            if i not in shape1:
                shape1[i]= 1
            if i in shape1:
                shape1[i]+=1
        keys = list(shape1.keys())
        values = list(shape1.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)  # create horizontal bar plot, will be the same for the rest of the shape section
        st.pyplot(fig)
    elif selectshape=="light":
        light = sdfShapes[sdfShapes["shape"] == "light"]
        shape2 = {}
        for i in light["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="circle":
        circle = sdfShapes[sdfShapes["shape"] == "circle"]
        shape2 = {}
        for i in circle["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="sphere":
        sphere = sdfShapes[sdfShapes["shape"] == "sphere"]
        shape2 = {}
        for i in sphere["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="disk":
        disk = sdfShapes[sdfShapes["shape"] == "disk"]
        shape2 = {}
        for i in disk["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="fireball":
        fireball = sdfShapes[sdfShapes["shape"] == "fireball"]
        shape2 = {}
        for i in fireball["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="unknown":
        unknown = sdfShapes[sdfShapes["shape"] == "unknown"]
        shape2 = {}
        for i in unknown["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="oval":
        oval = sdfShapes[sdfShapes["shape"] == "oval"]
        shape2 = {}
        for i in oval["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="other":
        other = sdfShapes[sdfShapes["shape"] == "other"]
        shape2 = {}
        for i in other["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="cigar":
        cigar = sdfShapes[sdfShapes["shape"] == "cigar"]
        shape2 = {}
        for i in cigar["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="rectangle":
        rectangle = sdfShapes[sdfShapes["shape"] == "rectangle"]
        shape2 = {}
        for i in rectangle["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="chevron":
        chevron = sdfShapes[sdfShapes["shape"] == "chevron"]
        shape2 = {}
        for i in chevron["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="triangle":
        triangle = sdfShapes[sdfShapes["shape"] == "triangle"]
        shape2 = {}
        for i in triangle["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="formation":
        formation = sdfShapes[sdfShapes["shape"] == "formation"]
        shape2 = {}
        for i in formation["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="delta":
        delta = sdfShapes[sdfShapes["shape"] == "delta"]
        shape2 = {}
        for i in delta["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="changing":
        changing = sdfShapes[sdfShapes["shape"] == "changing"]
        shape2 = {}
        for i in changing["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="egg":
        egg = sdfShapes[sdfShapes["shape"] == "egg"]
        shape2 = {}
        for i in egg["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="diamond":
        diamond = sdfShapes[sdfShapes["shape"] == "diamond"]
        shape2 = {}
        for i in diamond["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="flash":
        flash = sdfShapes[sdfShapes["shape"] == "flash"]
        shape2 = {}
        for i in flash["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="teardrop":
        teardrop = sdfShapes[sdfShapes["shape"] == "teardrop"]
        shape2 = {}
        for i in teardrop["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="cone":
        cone = sdfShapes[sdfShapes["shape"] == "cone"]
        shape2 = {}
        for i in cone["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="cross":
        cross = sdfShapes[sdfShapes["shape"] == "cross"]
        shape2 = {}
        for i in cross["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="pyramid":
        pyramid = sdfShapes[sdfShapes["shape"] == "pyramid"]
        shape2 = {}
        for i in pyramid["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="round":
        round = sdfShapes[sdfShapes["shape"] == "round"]
        shape2 = {}
        for i in round["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="crescent":
        crescent = sdfShapes[sdfShapes["shape"] == "crescent"]
        shape2 = {}
        for i in crescent["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="flare":
        flare = sdfShapes[sdfShapes["shape"] == "flare"]
        shape2 = {}
        for i in flare["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="hexagon":
        hexagon = sdfShapes[sdfShapes["shape"] == "hexagon"]
        shape2 = {}
        for i in hexagon["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="dome":
        dome = sdfShapes[sdfShapes["shape"] == "dome"]
        shape2 = {}
        for i in dome["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    elif selectshape=="changed":
        changed = sdfShapes[sdfShapes["shape"] == "changed"]
        shape2 = {}
        for i in changed["country"]:
            if i not in shape2:
                shape2[i]= 1
            if i in shape2:
                shape2[i]+=1
        keys = list(shape2.keys())
        values = list(shape2.values())
        fig,ax = plt.subplots()
        ax.barh(keys,values)
        st.pyplot(fig)
    st.write("The option \"nan\" means the data point was not given a country location")  # in these can't pop the empty cells in country so explain them
elif selectoptions == "Locations":  # new section based on location
    st.title("Where UFO Sightings Take Place")
    st.write("*This is not a comprehensive country list, the data file did not include all countries where sightings occured*")
    sdfLocation = dfUFO1.loc[:,["city","state","country"]]  # create smaller dataframe for this section
    countries = {}
    for i in sdfLocation["country"]:  # count sightings in each country in total
        if i not in countries:
            countries[i]= 1
        if i in countries:
            countries[i]+=1
    countries.pop("nan")
    countrykeys = list(countries.keys())
    countryvalues = list(countries.values())
    selectcountry = st.sidebar.selectbox("Do you want to see how sightings were spread out between states/provinces in US and CA?",["","US","CA"])
    # select box only has 3 options because the city list was not clear or tidy, and only two countries has states/provinces
    if selectcountry == "":  # section for pie chart of all data of sightings ascribed to a country
        fig, ax = plt.subplots()
        ax.pie(countryvalues,labels = countrykeys,textprops={'size': 'x-small'})
        ax.set_title("Distribution of UFO Sightings by Country")
        st.pyplot(fig)
    elif selectcountry=="US":  # US state sighting amount section
        states = {}
        USstates = sdfLocation[sdfLocation["country"] == "us"]  # isolates data frame to only US info
        #fl_df = df_employees[df_employees["salary"]>=10000]
        for i in USstates["state"]:  # counting per state
            if i not in states:
                states[i]=1
            if i in states:
                states[i]+=1
        keys = list(states.keys())
        values = list(states.values())
        fig, ax = plt.subplots()
        ax.bar(keys,values)
        ax.set_title("The Amount of UFO Sightings by State")
        ax.set_xlabel("States")
        ax.set_ylabel("Amount per State")
        plt.xticks(rotation=90, fontsize = 7)
        st.pyplot(fig)
    elif selectcountry=="CA":
        state2 = {}
        CAstates = sdfLocation[sdfLocation["country"] == "ca"]
        for i in CAstates["state"]:
            if i not in state2:
                state2[i]=1
            if i in state2:
                state2[i]+=1
        state2.pop("nan")
        keys = list(state2.keys())
        values = list(state2.values())
        fig,ax = plt.subplots()
        ax.bar(keys,values)
        ax.set_title("The Amount of UFO Sightings by Province")
        ax.set_xlabel("Provinces")
        ax.set_ylabel("Amount per Province")
        st.pyplot(fig)

