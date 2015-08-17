# PokemonAPI-Flask

## Overview

A simple API for getting Pokemon data. Written in Python using Flask-RESTful and MongoDB (alongside PyMongo).

## API Reference

#### Get regional Pokedex

Return the regional Pokedex (718 Pokemon) in JSON format.

**GET** /pokemon/api/v1.0/pokedex 

Each object these fields:

- name
- national_id
- primary_type
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
- dragon_egg_group
- mineral_egg_group
- amorphous_egg_group
- field_egg_group
- undiscovered_egg_group
- flying_egg_group
- water1_egg_group
- water2_egg_group
- water3_egg_group
- humanlike_egg_group
- ditto_egg_group
- grass_egg_group
- secondary_type
- fairy_egg_group
- monster_egg_group
- male_ratio
- egg_cycles
- female_ratio
- base_happiness

#### Get regional Pokedex

Returns the Pokedex of the given region (Kanto, Johto, Hoenn, Sinnoh, Unova and Kalos).

**GET** /pokemon/api/v1.0/pokedex/{region}

## Notes

This is a work in progress. I will be adding new features to the API in the future. Also, the API is not available online yet.

## Things I have in mind

- Make a field named egg_group with the egg group of each Pokemon, instead of having all the egg groups
as a Boolean field.

## Project

This repository contains a single Python file (the API) and an export of the collection (pokemondataset.json).
