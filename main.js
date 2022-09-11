async function getUserData() {
    return fetch('users.txt').then(response => response.text())
}

async function getUsers() {
    const userStrings = (await getUserData()).split(/\r?\n/)
    const userData = userStrings.map(string => string.split(', '))

    return userData.map(user => ({
        username: user[0],
        paygrade: user[1],
        funds: user[2],
    }))
}

function addUsersToTable(users) {
    const tableBody = document.querySelector('tbody')
    users.forEach(user => {
        const userRow = document.createElement('tr')
        for (const datum in user) {
            const tableData = document.createElement('td')
            tableData.innerText = user[datum]
            userRow.append(tableData)
        }
        tableBody.append(userRow)
    })
}

const sortingOptions = {
    Alphabet: 'username',
    Funds: 'funds',
}

async function main() {
    const users = await getUsers()
    users.sort((first, second) => {
        return first.username.localeCompare(second.username)
    })
    addUsersToTable(users)
}

window.addEventListener('DOMContentLoaded', main)
