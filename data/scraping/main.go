package main

import (
	"encoding/json"
	"fmt"
	"log"
	"os"
	"time"

	youtubescraper "github.com/PChaparro/go-youtube-scraper"
	ysi "github.com/PChaparro/go-youtube-scraper/interfaces"
	"github.com/joho/godotenv"
)

func main() {
	// Load environment variables
	err := godotenv.Load()

	if err != nil {
		log.Fatal("Unable to load environment variables")
	}

	// Get youtube api key from environment
	ytkey := os.Getenv("YOUTUBE_API_KEY")

	if ytkey == "" {
		log.Fatal("Youtube api key is not defined")
	}

	// Queries
	queue := [14]string{
		"Learn web development",
		"Latin music",
		"Best places to visit in Colombia",
		"Top new games of 2022",
		"Impossible moments in sports",
		"Cooking recipes",
		"Software development frameworks and methodologies",
		"Programming languages comparison",
		"Try not to laugh",
		"Learn data science",
		"Learn languages",
		"Looney Tunes Clasics",
		"Best carnivals in the world",
		"Open source software",
	}

	// Get results from youtube
	results := []ysi.Video{}

	for _, query := range queue {
		start := time.Now()

		queryResults, err := youtubescraper.GetVideosData(ytkey, query, 150, 64, true)

		if err != nil {
			log.Fatal(fmt.Sprintf("There was an error with the query: %s", query))
		}

		results = append(results, queryResults.Videos...)
		fmt.Printf("%s query took %v\n", query, time.Since(start))
	}

	// Parse to json
	json, err := json.Marshal(results)

	if err != nil {
		log.Fatal("Error when Marshal results")
	}

	// Save on local json file
	err = os.WriteFile("data.json", json, 0666)
}
