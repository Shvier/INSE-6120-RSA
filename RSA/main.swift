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
        let maxDivider = Int(sqrt(Double(self)))
        return !stride(from: 3, through: maxDivider, by: 2).contains { divider in
            return self % divider == 0
        }
    }
}

class RSAResolver {
    let p: Int
    let q: Int
    let N: Int
    let e: Int
    
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
        var m = max(left, right)
        var n = min(left, right)
        var remain = n
        while remain != 0 {
            remain = m % n
            m = n
            n = remain
        }
        return m
    }
    
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
        assert(e < phi, "failed to find e")
        self.e = e
    }
}

let resolver = RSAResolver()
print(resolver.p, resolver.q, resolver.N, resolver.e)
