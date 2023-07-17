import './App.css';

function App() {
  return (
    <div className="App">
      <form>
        <label>
          Tweet:
          <input type="text" name="tweet_post" />
        </label>
        <input type="submit" value="Post Tweet" />
      </form>
    </div>
  );
}

export default App;
