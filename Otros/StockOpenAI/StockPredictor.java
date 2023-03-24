package StockOpenAI;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class StockPredictor {

    private static final String STOCK_PRICE_API_URL = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=%s&apikey=CKNIDXVYUPBX98TB";

    public static void main(String[] args) {
        
        List<String> stockSymbols = getStockSymbols();

        List<Stock> stocks = new ArrayList<>();
        for (String stockSymbol : stockSymbols) {
            Stock stock = getStock(stockSymbol);
            if (stock != null) {
                stocks.add(stock);
            }
        }

        // Sort the stocks by their growth potential in descending order
        Collections.sort(stocks, (s1, s2) -> Double.compare(s2.getGrowthPotential(), s1.getGrowthPotential()));

        // Print the top 10 stocks with the highest growth potential
        for (int i = 0; i < 10 && i < stocks.size(); i++) {
            Stock stock = stocks.get(i);
            System.out.println(String.format("%s: %.2f%%", stock.getSymbol(), stock.getGrowthPotential()));
        }
    }

    private static Stock getStock(String stockSymbol) {
        try {
            System.out.println("Start");
            URL url = new URL(String.format(STOCK_PRICE_API_URL, stockSymbol));
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");

            BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            String response = reader.lines().collect(Collectors.joining());

            // Parse the response and calculate the growth potential
            double currentPrice = Double.parseDouble(getValueFromResponse(response, "05. price"));
            double yearLow = Double.parseDouble(getValueFromResponse(response, "09. 52 Week Low"));
            double yearHigh = Double.parseDouble(getValueFromResponse(response, "08. 52 Week High"));

            double growthPotential = (currentPrice - yearLow) / (yearHigh - yearLow) * 100;

            return new Stock(stockSymbol, growthPotential);
        } catch (Exception e) {
            System.out.println("Error");
            e.printStackTrace();
            return null;
        }
    }

    private static String getValueFromResponse(String response, String key) {
        int startIndex = response.indexOf(key);
        if (startIndex == -1) {
            return null;
        }
        startIndex = response.indexOf(':', startIndex);
        if (startIndex == -1) {
            return null;
        }
        startIndex += 2; // move past the ':' and '"'

        int endIndex = response.indexOf('"', startIndex);
        if (endIndex == -1) {
            return null;
        }

        return response.substring(startIndex, endIndex);
    }

    private static final String STOCK_SYMBOL_SEARCH_API_URL = "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=%s&apikey=CKNIDXVYUPBX98TB";

    private static List<String> getStockSymbols() {
        try {
            // Replace "keywords" in the URL with the search term that you want to use
            URL url = new URL(String.format(STOCK_SYMBOL_SEARCH_API_URL, "type:stocks"));
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
    
            BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            String response = reader.lines().collect(Collectors.joining());
    
            // Parse the response and extract the stock symbols
            List<String> stockSymbols = new ArrayList<>();
            int startIndex = 0;
            while (true) {
                int symbolStartIndex = response.indexOf("symbol", startIndex);
                if (symbolStartIndex == -1) {
                    break;
                }
                symbolStartIndex = response.indexOf(':', symbolStartIndex);
                if (symbolStartIndex == -1) {
                    break;
                }
                symbolStartIndex += 2; // move past the ':' and '"'
                int symbolEndIndex = response.indexOf('"', symbolStartIndex);
                if (symbolEndIndex == -1) {
                    break;
                }
    
                String symbol = response.substring(symbolStartIndex, symbolEndIndex);
                stockSymbols.add(symbol);
    
                startIndex = symbolEndIndex;
            }
    
            return stockSymbols;
        } catch (Exception e) {
            e.printStackTrace();
            return Collections.emptyList();
        }
    }
    
    

    private static class Stock {
        private String symbol;
        private double growthPotential;

        public Stock(String symbol, double growthPotential) {
            this.symbol = symbol;
            this.growthPotential = growthPotential;
        }

        public String getSymbol() {
            return symbol;
        }

        public double getGrowthPotential() {
            return growthPotential;
        }
    }
}
