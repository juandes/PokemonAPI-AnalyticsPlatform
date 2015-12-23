# PokemonAPI-Flask

## Overview

A simple API for getting Pokemon data. Written in Python using Flask-RESTful and MongoDB (alongside PyMongo).

## API Reference

#### Get national Pokedex

Return the national Pokedex (718 Pokemon) in JSON format.

**GET** /pokemon/api/v1.0/pokedex 

Each object these fields:

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

#### Get regional Pokedex

Returns the Pokedex of a specific region (Kanto, Johto, Hoenn, Sinnoh, Unova and Kalos).

**GET** /pokemon/api/v1.0/pokedex/{region}

## Notes

This is a work in progress. I will be adding new features to the API in the future. Also, the API is not available online yet.

## Things I have in mind

- Add an endpoint that returns a specific Pokemon (by name or national id).
- Add Diancie and Hoopa to the database.

## Project

This repository contains a single the API (app.py), several scripts, and an export of the collection (pokemondataset.json).
