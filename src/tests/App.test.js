import { render, screen } from '@testing-library/react'
import App from '../App'

test('Basic App rendering', async() => {
    render(<App/>)
    const linkElement = screen.getByText(/hello world/i);
    expect(linkElement).toBeInTheDocument();
})