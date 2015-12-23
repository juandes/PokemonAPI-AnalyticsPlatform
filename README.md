# PokemonAPI-AnalyticsPlatform

## Overview

My vision for this project is to have a data analysis platform that uses Pokemon data. So far it just has an API for getting Pokemon data. The long term goal is to have a more complete platform containing statistics, visualization, and machine learning applications about the series.

The platform is written in Python using Flask and MongoDB (alongside PyMongo).

## API Reference

#### Get Pokemon
Returns an specific Pokemon by either its national id or name
**GET** pokemon/api/v1.0/pokemon/{national_id}
**GET** pokemon/api/v1.0/pokemon/{name}

Each Pokemon has the following fields:
- name
- national_id
- primary_type
- secondary_type
- height
- weight
- region
- base_experience
- catch_rate
- hp
- attack
- special_attack
- defense
- special_defense
- speed
- total
- hp_ev
- attack_ev
- special_attack_ev
- defense_ev
- special_defense_ev
- speed_ev
- egg_groups
- male_ratio
- egg_cycles
- female_ratio
- base_happiness

### Get national Pokedex
Returns the national Pokedex (718 Pokemon) in JSON format.
**GET** /pokemon/api/v1.0/pokedex 

#### Get regional Pokedex
Returns the Pokedex of a specific region (Kanto, Johto, Hoenn, Sinnoh, Unova and Kalos).
**GET** /pokemon/api/v1.0/pokedex/{region}

## Notes

This is a work in progress. I will be adding new features to the API, and to the platform in general in the future. Also, the API is not available online yet.


## Project

This repository contains a single file (app.py) that has the web service code and the navigation of the application, several scripts used to transform the data, a template folder with the HTML code of the application,  and an export of the collection (pokemondataset.json).
