import { CompilerConfig } from '@ton/blueprint';

export const compile: CompilerConfig = {
    lang: 'tact',
    target: 'contracts/test_contract.tact',
    options: {
        debug: true,
    },
};
