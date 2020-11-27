import robin_stocks as rs
import mysql.connector
import os


def fetch_positions(uid, user, password):
    rs.login(username=user,
             password=password,
             expiresIn=86400,
             by_sms=True)
    res = []
    for ticker, pos in rs.account.build_holdings().items():
        res.append((uid, ticker, pos['price'], pos['quantity'], pos['average_buy_price'],
                    pos['equity'], pos['percent_change'], pos['equity_change'], pos['percentage'],))
    # print(res)
    return res


def main():
    db = mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST"),
        user=os.environ.get("MYSQL_USER"),
        password=os.environ.get("MYSQL_PASSWORD"),
        database=os.environ.get("MYSQL_DATABASE"),
        port=os.environ.get("MYSQL_PORT")
    )
    user = os.environ.get('RH_USER')
    password = os.environ.get('RH_PASS')
    conn = db.cursor()
    conn.execute("SELECT id FROM users WHERE name = %s", (user,))
    uid = conn.fetchone()[0]
    sql = "INSERT INTO `holdings` (`id`, `user`, `ticker`, `price`, `quantity`, `average_buy_price`, `equity`, `percent_change`, `equity_change`, `percentage`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    conn.executemany(sql, fetch_positions(uid, user, password))
    db.commit()


if __name__ == '__main__':
    main()
