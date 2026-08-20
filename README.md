# ⚽ FPL Machine Learning Model

A machine learning model for predicting Fantasy Premier League player points using historical player, fixture, form, and market data.

The model uses **XGBoost** to turn historical FPL data into player point projections, with a focus on recent form, playing time, player value, and market behaviour.

> Raw historical data sourced from https://github.com/vaastav/Fantasy-Premier-League.

## Overview

- **133k+** player-gameweek records
- Historical data spanning multiple FPL seasons
- **XGBoost** regression model
- **RMSE of 2.58** on the current evaluation setup

## Features

The model combines several sources of information to estimate expected player performance:

- Player performance and match statistics
- Recent form
- Playing time and starting consistency
- Player value
- Transfer activity
- Team and season context

## Feature Engineering

The pipeline transforms raw FPL data into features that capture current performance and historical context.

Key steps include:

- Previous-match statistics
- Rolling form features
- Player and team encoding
- Cross-season player tracking
- Handling missing historical statistics

The model is designed to use information available before a gameweek when generating predictions.

## Machine Learning

The project uses **XGBoost**, a gradient-boosted decision tree algorithm suited to structured data.

Model development and evaluation are handled using **XGBoost** and **Scikit-learn**, with **Pandas** and **NumPy** used throughout the data pipeline.

## What Drives Predictions?

Some of the strongest signals identified by the model include:

- **Player value** — a proxy for expected performance
- **Transfer activity** — a signal of FPL manager sentiment
- **Minutes played** — an indicator of playing-time security
- **Recent form** — capturing short-term performance trends

## Tech Stack

**Python**  
Pandas · NumPy · XGBoost · Scikit-learn

## Goal

The goal is to build a data-driven FPL prediction system that can help evaluate player performance and support decisions around **transfers, squad selection, captaincy, and gameweek planning**.
