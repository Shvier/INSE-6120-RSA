//
//  main.swift
//  RSA
//
//  Created by Barry Lee on 2022-10-08.
//

import Foundation

extension Int {
    func isPrime() -> Bool {
        if self == 2 { return true }
        guard self > 1 && self % 2 != 0 else { return false }
        let maxFactor = Int(sqrt(Double(self)))
        return !stride(from: 3, through: maxFactor, by: 2).contains { factor in
            return self % factor == 0
        }
    }
}

class RSAResolver {
    private class func generatePrimeNumber() -> Int {
        let lower: Int = 2 << 14
        let upper: Int = 2 << 15
        while true {
            let probablePrime = Int.random(in: lower..<upper)
            if probablePrime.isPrime() {
                return probablePrime
            }
        }
    }
    
    private class func gcd(_ left: Int, _ right: Int) -> Int {
        var dividend = max(left, right)
        var divisor = min(left, right)
        var remainder = divisor
        while remainder != 0 {
            remainder = dividend % divisor
            dividend = divisor
            divisor = remainder
        }
        return dividend
    }
    
    private class func findMultiInverse(_ e: Int, _ phi: Int) -> Int {
        var dividend = max(e, phi)
        var divisor = min(e, phi)
        var x1 = 1
        var x2 = 0
        while divisor != 1 {
            let quotient = dividend / divisor
            let remainder = dividend - quotient * divisor
            let x = x2 - quotient * x1
            dividend = divisor
            divisor = remainder
            x2 = x1
            x1 = x
        }
        return x1 >= 0 ? x1 : x1 + phi
    }
    
    private let p: Int
    private let q: Int
    private let d: Int

    let N: Int
    let e: Int
    
    init() {
        let p = RSAResolver.generatePrimeNumber()
        var q = RSAResolver.generatePrimeNumber()
        while p == q {
            q = RSAResolver.generatePrimeNumber()
        }
        self.p = p
        self.q = q
        self.N = p * q
        let phi = (p - 1) * (q - 1)
        var e = 2 << 15 + 1
        while RSAResolver.gcd(phi, e) != 1 {
            e = e + 2
        }
        assert(e < phi, "Failed to find e")
        self.e = e
        let d = RSAResolver.findMultiInverse(e, phi)
        self.d = d
        print("p: \(self.p), q: \(self.q), d: \(self.d)")
    }
}

let resolver = RSAResolver()
print("(e, N): (\(resolver.e), \(resolver.N))")
